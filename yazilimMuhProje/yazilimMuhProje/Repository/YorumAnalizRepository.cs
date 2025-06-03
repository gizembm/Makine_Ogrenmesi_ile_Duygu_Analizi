using System;
using System.Collections.Generic;
using System.Data.Entity;
using System.Linq;
using System.Web;
using yazilimMuhProje.Models.Entities;

namespace yazilimMuhProje.Repository
{
    public class YorumAnalizRepository : GenericRepositories<YorumAnaliz>
    {
        private duyguAnalizDBEntities _context;

        public YorumAnalizRepository()
        {
            _context = new duyguAnalizDBEntities(); 
        }

        // Yeni analiz kaydı ekleme metod
        public void TAdd(YorumAnaliz analiz)
        {
            _context.YorumAnaliz.Add(analiz);
            _context.SaveChanges();
        }
    }
}