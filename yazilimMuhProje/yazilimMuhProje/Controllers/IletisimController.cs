using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using yazilimMuhProje.Models.Entities;
using yazilimMuhProje.Repository;

namespace yazilimMuhProje.Controllers
{
    public class IletisimController : Controller
    {
        // GET: Iletisim
        private readonly GenericRepositories<Iletisim> iletisimRepo = new GenericRepositories<Iletisim>();

        public ActionResult Index()
        {
            return View();
        }

        [HttpPost]
        public ActionResult Index(Iletisim iletisim)
        {
            if (ModelState.IsValid)
            {
                // E-posta geçerliliğini kontrol et
                var allowedDomains = new[] { "@gmail.com", "@hotmail.com", "@outlook.com" };
                if (!allowedDomains.Any(domain => iletisim.Eposta.EndsWith(domain)))
                {
                    ModelState.AddModelError("Eposta", "Geçersiz e-posta domain'i. Lütfen @gmail.com, @hotmail.com veya @outlook.com gibi domainler kullanın.");
                    return View(iletisim);
                }

                try
                {
                   
                    iletisim.KayitTarihi = DateTime.Now;
                    iletisimRepo.TAdd(iletisim);
                    ViewBag.Mesaj = "Mesajınız başarıyla gönderildi!";
                    return View();
                }
                catch (Exception ex)
                {
                    // Hata mesajını kullanıcıya ilet
                    ViewBag.Mesaj = "Bir hata oluştu: " + ex.Message;
                    return View(iletisim);
                }
            }

            
            ViewBag.Mesaj = "Lütfen geçerli bir e-posta adresi girin.";
            return View(iletisim);
        }



    }
}