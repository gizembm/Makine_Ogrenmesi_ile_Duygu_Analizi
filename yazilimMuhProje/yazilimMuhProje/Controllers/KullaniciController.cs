using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using yazilimMuhProje.Models.Entities;
using yazilimMuhProje.Repository;

namespace yazilimMuhProje.Controllers
{
    public class KullaniciController : Controller
    {
        // GET: Kullanici
        private readonly GenericRepositories<Kullanicilar> kullaniciRepo = new GenericRepositories<Kullanicilar>();

        //Kayıt ol sayfası
        public ActionResult KayitOl()
        {
            return View();
        }

        [HttpPost]
        public ActionResult KayitOl(Kullanicilar kullanici, string SifreOnay)
        {
            if (ModelState.IsValid)
            {
                
                var allowedDomains = new[] { "@gmail.com", "@hotmail.com", "@outlook.com" };
                if (!allowedDomains.Any(domain => kullanici.Eposta.EndsWith(domain)))
                {
                    ModelState.AddModelError("Eposta", "Geçersiz e-posta domain'i. Lütfen @gmail.com, @hotmail.com veya @outlook.com gibi domainler kullanın.");
                    return View(kullanici);
                }

                // Şifre ve şifre onayı eşleşiyor mu?
                if (kullanici.Sifre != SifreOnay)
                {
                    ModelState.AddModelError("", "Şifreler eşleşmiyor.");
                    return View(kullanici);
                }

                
                if (kullanici.Sifre.Length != 8)
                {
                    ModelState.AddModelError("Sifre", "Şifre 8 karakterden oluşmalıdır.");
                    return View(kullanici);
                }

                
                kullanici.KayitTarihi = DateTime.Now;
                kullaniciRepo.TAdd(kullanici);

                return RedirectToAction("Giris");
            }

            return View(kullanici);
        }



        // Giriş Yap Sayfası
        public ActionResult Giris()
        {
            return View();
        }

        [HttpPost]
        public ActionResult Giris(string Eposta, string Sifre)
        {
            var kullanici = kullaniciRepo.Find(k => k.Eposta == Eposta && k.Sifre == Sifre);
            if (kullanici != null)
            {
                Session["KullaniciId"] = kullanici.KullaniciId;
                Session["KullaniciAdi"] = kullanici.KullaniciAdi;
                return RedirectToAction("Index", "Home"); // Ana sayfaya yönlendir
            }
            else
            {
                ModelState.AddModelError("", "Eposta veya şifre hatalı.");
                return View();
            }
        }


        // Şifremi Unuttum Sayfası
        public ActionResult SifremiUnuttum()
        {
            return View();
        }

        [HttpPost]
        public ActionResult SifremiUnuttum(string Eposta, string YeniSifre, string SifreOnay)
        {
            var kullanici = kullaniciRepo.Find(k => k.Eposta == Eposta);

            if (kullanici == null)
            {
                ModelState.AddModelError("Eposta", "Bu e-posta adresine ait bir hesap bulunamadı. Lütfen bir hesap oluşturun.");
                return View();
            }

            if (YeniSifre != SifreOnay)
            {
                ModelState.AddModelError("SifreOnay", "Şifreler eşleşmiyor."); // Sadece şifre tekrar alanının altında görünür
                return View();
            }

            if (YeniSifre.Length != 8)
            {
                ModelState.AddModelError("YeniSifre", "Şifre 8 karakterden oluşmalıdır."); // Sadece şifre alanının altında görünür
                return View();
            }

            kullanici.Sifre = YeniSifre;
            kullaniciRepo.TUpdate(kullanici);

            ViewBag.Mesaj = "Şifreniz başarıyla güncellendi. Şimdi giriş yapabilirsiniz.";
            return RedirectToAction("Giris");
        }


        // Çıkış Yap
        public ActionResult Cikis()
        {
            Session.Clear();
            return RedirectToAction("Index", "Home");
        }


    }
}
