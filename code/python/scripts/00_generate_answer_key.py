import pandas as pd

answer_key = pd.DataFrame([
    {
        "deal_id": 1,
        "acquirer": "Pfizer Inc.",
        "target": "Wyeth",

        "name_change_occurred": False,
        "name_change_date": None,
        "resulting_public_company_name": "Pfizer Inc.",

        "public_company_that_ceased_trading": "Wyeth",
        "ceased_public_date": "2009-10-15",

        "agreement_date": "2009-01-25",
        "closing_date": "2009-10-15",

        "agreement_source": "https://www.pfizer.com/news/press-release/press-release-detail/pfizer_to_acquire_wyeth_creating_the_world_s_premier_biopharmaceutical_company",
        "closing_source": "https://www.pfizer.com/news/press-release/press-release-detail/pfizer_completes_acquisition_of_wyeth",
        "public_status_source": "https://www.pfizer.com/news/press-release/press-release-detail/pfizer_completes_acquisition_of_wyeth",
        "name_source": None,

        "notes": None
    },
    
    { 
        "deal_id": 2,
        "acquirer": "Merck & Co., Inc. (Old Merck)",
        "target": "Schering-Plough Corporation",

        "name_change_occurred": True,
        "name_change_date": "2009-11-03",
        "resulting_public_company_name": 'Merck & Co., Inc.',

        "public_company_that_ceased_trading": "Merck & Co., Inc. (Old Merck)",
        "ceased_public_date": "2009-11-03",

        "agreement_date": "2009-03-08",
        "closing_date": "2009-11-03",

        "agreement_source": "https://web.archive.org/web/20090311235556/http://www.merck.com/newsroom/press_releases/corporate/2009_0309.html",
        "closing_source": "https://web.archive.org/web/20091107063055/http://www.merck.com/newsroom/news-release-archive/corporate/2009_1103.html",
        "public_status_source": "https://web.archive.org/web/20091107063055/http://www.merck.com/newsroom/news-release-archive/corporate/2009_1103.html",
        "name_source": "https://web.archive.org/web/20091107063055/http://www.merck.com/newsroom/news-release-archive/corporate/2009_1103.html",

        "notes": "Two-step reverse merger. Schering-Plough survived the first merger and was renamed Merck & Co., Inc. Merck survived the second merger and became a wholly owned subsidiary, renamed Merck Sharp & Dohme Corp."
    },

    {
        "deal_id": 3,
        "acquirer": "Roche",
        "target": "Genentech, Inc.",

        "name_change_occurred": False,
        "name_change_date": None,
        "resulting_public_company_name": "Roche",

        "public_company_that_ceased_trading": "Genentech, Inc.",
        "ceased_public_date": "2009-03-26",

        "agreement_date": "2009-03-12",
        "closing_date": "2009-03-26",

        "agreement_source": "https://assets.cwp.roche.com/f/126832/x/f0613a673d/rhi_hy_2010.pdf",
        "closing_source": "https://assets.cwp.roche.com/f/126832/x/f0613a673d/rhi_hy_2010.pdf",
        "public_status_source": "https://assets.cwp.roche.com/f/126832/x/f0613a673d/rhi_hy_2010.pdf",
        "name_source": None,

        "notes": None
    },
    {
        "deal_id": 4,
        "acquirer": "Sanofi-Aventis",
        "target": "Genzyme Corporation",

        "name_change_occurred": True,
        "name_change_date": "2011-06-15",
        "resulting_public_company_name": "Sanofi",

        "public_company_that_ceased_trading": "Genzyme Corporation",
        "ceased_public_date": "2011-04-08",

        "agreement_date": "2011-02-16",
        "closing_date": "2011-04-08",

        "agreement_source": "https://www.prnewswire.com/news-releases/sanofi-aventis-to-acquire-genzyme-for-7400-in-cash-per-share-plus-contingent-value-right-116291094.html",
        "closing_source": "https://www.prnewswire.com/news-releases/sanofi-aventis-completes-acquisition-of-genzyme-corporation-119496769.html",
        "public_status_source": "https://www.prnewswire.com/news-releases/sanofi-aventis-completes-acquisition-of-genzyme-corporation-119496769.html",
        "name_source": "https://www.news.sanofi.us/Sanofi-Media-Statement-in-Response-to-Inquiries-Following-Announcement-of-Logo-Change-in-North-America-on-June-15-2011",

        "notes": "Sanofi-Aventis changed its name to Sanofi in 2011, after the acquisition of Genzyme"
    },
    {
        "deal_id": 5,
        "acquirer": "Gilead Sciences, Inc.",
        "target": "Pharmasset, Inc.",

        "name_change_occurred": False,
        "name_change_date": None,
        "resulting_public_company_name": "Gilead Sciences, Inc.",

        "public_company_that_ceased_trading": "Pharmasset, Inc.",
        "ceased_public_date": "2012-01-17",

        "agreement_date": "2011-11-21",
        "closing_date": "2012-01-17",

        "agreement_source": "https://www.gilead.com/news/news-details/2011/gilead-sciences-to-acquire-pharmasset-inc-for-11-billion",
        "closing_source": "https://www.gilead.com/news/news-details/2012/gilead-sciences-completes-acquisition-of-pharmasset-inc",
        "public_status_source": "https://www.gilead.com/news/news-details/2012/gilead-sciences-completes-acquisition-of-pharmasset-inc",
        "name_source": None,

        "notes": "The tender offer closed 2012-01-12"
    },
    {
        "deal_id": 6,
        "acquirer": "Actavis plc",
        "target": "Allergan, Inc.",

        "name_change_occurred": True,
        "name_change_date": "2015-06-15",
        "resulting_public_company_name": "Allergan plc",

        "public_company_that_ceased_trading": "Allergan, Inc.",
        "ceased_public_date": "2015-03-17",

        "agreement_date": "2014-11-17",
        "closing_date": "2015-03-17",

        "agreement_source": "https://www.fiercepharma.com/m-a/actavis-to-acquire-allergan-to-create-top-10-global-growth-pharmaceutical-company-23-billion",
        "closing_source": "https://www.prnewswire.com/news-releases/actavis-completes-allergan-acquisition-300051633.html",
        "public_status_source": "https://www.prnewswire.com/news-releases/actavis-completes-allergan-acquisition-300051633.html",
        "name_source": "https://www.prnewswire.com/news-releases/actavis-plc-is-now-allergan-plc-300098692.html",

        "notes": None
    },
    {
        "deal_id": 7,
        "acquirer": "Teva Pharmaceutical Industries Ltd.",
        "target": "Allergan's global generics business",
        
        "name_change_occurred": False,
        "name_change_date": None,
        "resulting_public_company_name": "Teva Pharmaceutical Industries Ltd.",

        "public_company_that_ceased_trading": None,
        "ceased_public_date": None,

        "agreement_date": "2015-07-27",
        "closing_date": "2016-08-02",

        "agreement_source": "https://ir.tevapharm.com/news-and-events/press-releases/press-release-details/2015/Teva-to-Acquire-Allergan-Generics-for-405-Billion-Creating-a-Transformative-Generics-and-Specialty-Company-Well-Positioned-to-Win-in-Global-Healthcare/default.aspx",
        "closing_source": "https://ir.tevapharm.com/news-and-events/press-releases/press-release-details/2016/Teva-Completes-Acquisition-of-Actavis-Generics/default.aspx",
        "public_status_source": None,
        "name_source": None,

        "notes": None
    },
    {
        "deal_id": 8,
        "acquirer": "Johnson & Johnson",
        "target": "Actelion Ltd.",
        
        "name_change_occurred": False,
        "name_change_date": None,
        "resulting_public_company_name" : "Johnson & Johnson",

        "public_company_that_ceased_trading": "Actelion Ltd.",
        "ceased_public_date": "2017-11-06",

        "agreement_date": "2017-01-26",
        "closing_date": "2017-06-16",

        "agreement_source": "https://www.jnj.com/media-center/press-releases/johnson-johnson-to-acquire-actelion",
        "closing_source": "https://www.jnj.com/media-center/press-releases/johnson-johnson-announces-completion-of-acquisition-of-actelion",
        "public_status_source": "https://www.biospace.com/cancellation-of-publicly-held-actelion-shares-and-delisting-from-six-swiss-exchange-as-of-november-7-2017",
        "name_source": None,

        "notes": "Actelion spun off its drug discovery and early-stage development business into Idorsia immediately before the tender offer settled."
    },
    { 
        "deal_id": 9,
        "acquirer": None,
        "target": None,
        
        "name_change_occurred": True,
        "name_change_date": "2018-07-13",
        "resulting_public_company_name": "Bausch Health Companies Inc.",

        "public_company_that_ceased_trading": None,
        "ceased_public_date": None,

        "agreement_date": None,
        "closing_date": None,

        "agreement_source": None,
        "closing_source": None,
        "public_status_source": None,
        "name_source": "https://ir.bauschhealth.com/news-releases/archive/2018/07-13-2018",

        "notes": "Control case; name change"
    },
    {
        "deal_id": 10,
        "acquirer": "Takeda Pharmaceutical Company Limited",
        "target": "Shire plc",
        
        "name_change_occurred": False,
        "name_change_date": None,
        "resulting_public_company_name": "Takeda Pharmaceutical Company Limited",

        "public_company_that_ceased_trading": "Shire plc",
        "ceased_public_date": "2019-01-08",

        "agreement_date": "2018-05-08",
        "closing_date": "2019-01-08",

        "agreement_source": "https://www.takeda.com/newsroom/newsreleases/2018/proposed-acquisition-of-shire-plc-by-takeda/",
        "closing_source": "https://www.takeda.com/newsroom/shire-news-releases/2019/qppcx8/",
        "public_status_source": "https://www.takeda.com/newsroom/shire-news-releases/2019/qppcx8/",
        "name_source": None,

        "notes": "Acquistion took place under scheme of arrangement"
    },
    {
        "deal_id": 11,
        "acquirer": "Bristol-Myers Squibb Company",
        "target": "Celgene Corporation",
        
        "name_change_occurred": False,
        "name_change_date": None,
        "resulting_public_company_name": "Bristol-Myers Squibb Company",

        "public_company_that_ceased_trading": "Celgene Corporation",
        "ceased_public_date": "2019-11-20",

        "agreement_date": "2019-01-03",
        "closing_date": "2019-11-20",

        "agreement_source": "https://news.bms.com/news/details/2019/Bristol-Myers-Squibb-to-Acquire-Celgene-to-Create-a-Premier-Innovative-Biopharma-Company/default.aspx",
        "closing_source": "https://news.bms.com/news/details/2019/Bristol-Myers-Squibb-Completes-Acquisition-of-Celgene-Creating-a-Leading-Biopharma-Company/default.aspx",
        "public_status_source": "https://news.bms.com/news/details/2019/Bristol-Myers-Squibb-Completes-Acquisition-of-Celgene-Creating-a-Leading-Biopharma-Company/default.aspx",
        "name_source": None,

        "notes": None
    },
    {
        "deal_id": 12,
        "acquirer": "AbbVie Inc.",
        "target": "Allergan plc",
        
        "name_change_occurred": False,
        "name_change_date": None,
        "resulting_public_company_name": "AbbVie Inc.",

        "public_company_that_ceased_trading": "Allergan plc",
        "ceased_public_date": "2020-05-08",
        
        "agreement_date": "2019-06-25",
        "closing_date": "2020-05-08",

        "agreement_source": "https://news.abbvie.com/2019-06-25-AbbVie-to-Acquire-Allergan-in-Transformative-Move-for-Both-Companies",
        "closing_source": "https://news.abbvie.com/2020-05-08-AbbVie-Completes-Transformative-Acquisition-of-Allergan",
        "public_status_source": "https://news.abbvie.com/2020-05-08-AbbVie-Completes-Transformative-Acquisition-of-Allergan",
        "name_source": None,

        "notes": "Acquistion took place under scheme of arrangement; not a conventional merger"
    },
    {
        "deal_id": 13,
        "acquirer": None,
        "target": None,
        
        "name_change_occurred": True,
        "name_change_date": "2020-11-16",
        "resulting_public_company_name": "Viatris inc.",

        "public_company_that_ceased_trading": "Mylan N.V.",
        "ceased_public_date": "2020-11-16",

        "agreement_date": "2019-07-29",
        "closing_date": "2020-11-16",

        "agreement_source": "https://www.pfizer.com/news/press-release/press-release-detail/mylan_and_upjohn_a_division_of_pfizer_to_combine_creating_a_new_champion_for_global_health_uniquely_positioned_to_fulfill_the_world_s_need_for_medicine",
        "closing_source": "https://www.pfizer.com/news/press-release/press-release-detail/pfizer-completes-transaction-combine-its-upjohn-business",
        "public_status_source": "https://www.pfizer.com/news/press-release/press-release-detail/pfizer-completes-transaction-combine-its-upjohn-business",
        "name_source": "https://www.pfizer.com/news/press-release/press-release-detail/pfizer-completes-transaction-combine-its-upjohn-business",

        "notes": "There is no clear cut acquirer-target relationship in this deal. Mylan and Upjohn both combined to form Viatris"
    },

    {
        "deal_id": 14,
        "acquirer": "AstraZeneca PLC",
        "target": "Alexion Pharmaceuticals, Inc.",

        "name_change_occurred": False,
        "name_change_date": None,
        "resulting_public_company_name": "AstraZeneca PLC",

        "public_company_that_ceased_trading": "Alexion Pharmaceuticals, Inc.",
        "ceased_public_date": "2021-07-20",
        
        "agreement_date": "2020-12-12",
        "closing_date": "2021-07-21",

        "agreement_source": "https://www.astrazeneca.com/media-centre/press-releases/2020/astrazeneca-to-acquire-alexion.html#!",
        "closing_source": "https://www.astrazeneca.com/media-centre/press-releases/2021/acquisition-of-alexion-completed.html#!",
        "public_status_source": "https://www.astrazeneca.com/media-centre/press-releases/2021/acquisition-of-alexion-completed.html#!",
        "name_source": None,

        "notes": None
    },

    {
        "deal_id": 15,
        "acquirer": "Amgen Inc.",
        "target": "Horizon Therapeutics plc",
        
        "name_change_occurred": False,
        "name_change_date": None,
        "resulting_public_company_name": "Amgen Inc.",

        "public_company_that_ceased_trading": "Horizon Therapeutics plc",
        "ceased_public_date": "2023-10-05",

        "agreement_date": "2022-12-12",
        "closing_date": "2023-10-06",

        "agreement_source": "https://investors.amgen.com/news-releases/news-release-details/rule-27-announcement-amgen-inc-acquire-horizon-therapeutics-plc",
        "closing_source": "https://www.amgen.com/newsroom/press-releases/2023/10/amgen-completes-acquisition-of-horizon-therapeutics-plc",
        "public_status_source": "https://www.nasdaqtrader.com/TraderNews.aspx?id=ECA2023-570",
        "name_source": None,

        "notes": None
    },

    {
        "deal_id": 16,
        "acquirer": "Pfizer Inc.",
        "target": "Seagen Inc.",
        
        "name_change_occurred": False,
        "name_change_date": None,
        "resulting_public_company_name": "Pfizer Inc.",

        "public_company_that_ceased_trading": "Seagen Inc.",
        "ceased_public_date": "2023-12-13",

        "agreement_date": "2023-03-13",
        "closing_date": "2023-12-14",

        "agreement_source": "https://www.pfizer.com/news/press-release/press-release-detail/pfizer-invests-43-billion-battle-cancer",
        "closing_source": "https://www.pfizer.com/news/press-release/press-release-detail/pfizer-completes-acquisition-seagen",
        "public_status_source": "https://www.nasdaqtrader.com/TraderNews.aspx?id=ECA2023-721",
        "name_source": None,

        "notes": None
    },
])

answer_key.to_csv(
    "data/answer_key.csv",
    index=False
)