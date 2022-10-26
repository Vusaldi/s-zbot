import random
kelimeler = ["gözəl","bilik","problem","təmin","ayrılmaq","zaman","susamaq","edin","istifadə","yox","bax",
              "axtarmaq", "dovşan", "amma", "manat", "oynamaq", "çiçək", "şəhər", "yüksək", "döyüş", "varlıq", "güvənmək",
              "güvən", "lazım", "müalicə", "şəhid", "rahat", "soyuq", "oradan", "kitab", "payız", "hesab", "bədən",
              'zəmin', 'dəmiz', 'sistem', 'gözləmək', 'çəkinmək', 'texnika', 'yaşlanmaq', 'gətirmək', 'tarix', 'dəqiq', 'başlıq',
              "cərimə", "əgər", "ancaq", "qaytarmaq", "vermək", "var", "qalıq", "şəxs", "başqa", "dövr", "yenidən", "bunlar",
              "kitab", "hadisə", "olmaq", "mübarizə", "dövlət", "ödəmək", "dəyişmək", "baxmaq", "divan", "belə", "bəzi", "başlamaq",
              "saxla", "pərdə", "biri", "etdirmək", "su", "bəyən", "bələdiyyə", "sağol", "orta", "dəyərsiz", "BÖYÜTMƏK", "etmək",
              "yeni", "əsəb", "soruşmaq", "döyüşmək", "yandırmaq", 'eşitmək', 'ikisi', "həmişə", "səsli", "inanmaq", "yoxlamaq", "saat", "necə",
              'bir', 'və', 'olmaq', 'bu', 'üçün', 'nəfəs', 'mən', 'demək', 'inək', 'vətən', 'nəsil', 'bəyənmək', 'döymək', 'almaq',
              'dəyərli', 'peşman', 'gülmək', 'birlikdə', 'vermək', 'amma', 'sonra', 'qədər', 'yer', 'çoxluq', 'insanlar', 'bizim', 'hər ', 'istəmək', 'il', 'çıxmaq', 'görmək', 'gün', 'biz', 'getmək', 'işləmək', 'yayım', 'oxşamaq', 'bilmək', 'sənətkar', 'zaman',
              'dinləmək', 'uşaq', 'iki', 'dözmək', 'birlik', 'səbr', 'böyük', 'sevilmək', 'başlanğıc', 'yol', 'qal', 'niyə', 'sən',
              'mövzu', 'ibarət', 'yaxşı', 'qadın', 'ev', 'olmaq', 'qeyrət', 'demək', 'göz', 'lazım', 'dünya',
              'yemək', 'heç', 'hətta', 'necə', 'hamısı', 'əleyhinə', 'tapmaq', 'belə', 'yaşamaq', 'düşünmək', 'eyni', 'içmək', 'lakin',
              'iman', 'onlar', 'birinci', 'görə', 'ölmək', 'son', 'bəhanə', 'forma', 'vacib', 'üz', 'futboı', 'göstərmək', 'etmək',
              'alma', 'günah', 'istifadə', 'çünkü', 'yan', 'indi', 'kişi', 'onun', 'başqası', 'xəyanət', 'bağışlamaq', 'oğur', 'həmişəlik',
              'sağ', 'durmaq', 'qız', 'hamısı', 'cəlb', 'göstəriş', 'danışmaq', 'pul', 'anlamaq', 'ana', 'ilan', 'bəzi', 'ata', 'həyat ',
              'yalnız', 'kiçik', 'daha', 'məlumat', 'keçirmək', 'soruş', 'hədiyyə', 'söyləmək', 'yenidən', 'təmin', 'nəticə', 'istifadə', 'xarici ',
              'kimsə', 'ordan', 'müddət', 'döndərmək', 'yanmaq', 'oturmaq', 'demək', 'çıxmaq', 'dərhal', 'vaxt', 'qruz', 'problem', 'dil',
              'həkim', 'sətir', 'yazmaq', 'faiz', 'aylıq', 'atmaq', 'tutmaq', 'qaydalar', 'hadisə', 'düşmək', 'eşitmək', 'sözü', 'gözəl',
              'sevmək', 'bir', 'çətin', 'almaq', 'itirmək', 'qoymaq', 'birləşmək', 'kimsə', 'birlikdə', 'veriləcək', 'kimsə', 'bayraq', 'gənc',
              'qapı', 'kitab', 'qeyrətli', 'burada', 'gecə', 'alan', 'divar', 'meydan', 'gözləyin', 'uzun', 'qış', 'günəş', 'axırıncı',
              'kimsə', 'məhsul', 'ailə', 'kimsəsiz', 'oxumaq', 'kişi', 'hamı', 'güc', 'bəlkə', 'real', 'tam', 'əlaqəli', 'münasibət ',
              'mühit', 'köhnə', 'axtarış', 'təbib', 'oğlu', 'yaxınlıq', 'küçə', 'tarix', 'mülkiyyət', 'bölmə', 'özəl', 'səbəbsiz',
              'heç', 'kim', 'çox', 'deyil', 'əgər', 'lazımsız', 'xüsusi', 'məna', 'yüksəlmə', 'bank', 'tərbiyə', 'dəfə', 'ayaq', 'hərəkət', 'geri', 'cəmiyyət',
              'alət', 'gitara', 'növ', 'qərar', 'internet', 'hava', 'nömrə', 'fərqli', 'qrup', 'otaq', 'topluq', 'xəbər', 'xəbərlər',
              'allah', 'həmçini', 'gələn', 'şeytan', 'sual', 'geri', 'qazanmaq', 'post', 'məktəb', 'açıq', 'öyrən', 'sürüş',
              'dil', 'şirkət', 'mənbə', 'bitir', 'proqram', 'davam', 'hərəkət', 'rəng', 'açmaq', 'sağ', 'inan',
              'təhsil', 'bucaq', 'parça', 'qəzet', 'tərifləmək', 'əlbət', 'dəyər', 'bilmək', 'bərbər', 'doktor', 'gəlir',
              'tapşırıq', 'məqsəd', 'region', 'film', 'iştirak', 'müştəri', 'artıq', 'telefon', 'təhsil', 'dəniz', 'ikinci',
              'qalx', 'hətta', 'təsir', 'inkişaf', 'keçmək', 'bədən', 'düşüncə', 'milyon', 'oynamaq', 'dəyişiklik', 'əsas',
              'yaratmaq', 'çatmaq', 'düşünmək', 'keçmək', 'mədəniyyət', 'qurmaq', 'amma', 'buna', 'rəsmi', 'etmək', 'işıqlandırmaq', 'içmək',
              'xanım', 'xidmət', 'ehtiyac', 'nöqtə', 'istiqamət', 'bəli', 'oyun', 'artırma', 'təkrar', 'proses', 'qısa', 'asan',
              'hansı', 'qiymət', 'əslində', 'qəbul', 'edirəm', 'orada', 'diqqət', 'uzaq', 'kompüter', 'gələcək', 'görünür',
              'məsələn', 'oğul', 'dinləmə', 'uyğun', 'lirə', 'istehsal', 'dəqiqə', 'unutmaq', 'gəzinti', 'belə', 'pis',
              'avtomobil', 'ağız', 'hiss', 'tətbiq', 'hələ', 'nümunə', 'işıq', 'baxmaq', 'dərəcə', 'mümkün', 'belə',
              'divar', 'onun', 'incəsənət', 'haqda', 'xəstəlik', 'tələbə', 'televiziya', 'metro', 'masa', 'ölüm', 'komanda', 'top',
              'baş', 'musiqi', 'ayrılmaq', 'enerji', 'universitet', 'idman', 'mehriban', 'insanlıq', 'baxmayaraq', 'hissə', 'ölüm',
              'daimi', 'sağlamlıq', 'müxtəlif', 'bundan', 'hiss', 'halbuki', 'səhər', 'internet', 'texniki', 'çıxış',
              'mərkəz', 'ekologiya', 'əvəzində', 'səviyyə', 'kənd', 'idarəetmə', 'aşağı', 'cavab', 'şir', 'torpaq', 'axşam', 'araşdırma', 'götürmək', 'iştirak', 'etmək', 'əks', 'qurmaq', 'ödəmək', 'sanki', 'qan', 'xəstə', 'şəhər', 'enmək',
              'indiki', 'məlum', 'həftə', 'trafik', 'hesab', 'avtomobil', 'planet', 'davranış', 'mətbəx', 'şəhər', 'bəzən',
              'müəyyən', 'ayrı', 'qiymət', 'haqqında', 'çıxarmaq', 'qol', 'yalnız', 'hazırlamaq', 'şüşə', 'nəhayət', 'yavaş',
              'zəruri', 'əhəmiyyət', 'xatirə', 'yalan', 'aktiv', 'sənət', 'faiz', 'diş', 'satış', 'təbi', 'öz',
              'iqtisadi', 'ağrı', 'yox', 'qorumaq', 'mərtəbə', 'iqtisadiyyat', 'ümumi', 'müəyyən ', 'foto', 'heyvan', 'müharibə',
              'mal', 'saç', 'itirmək', 'qalıq', 'dəyişiklik', 'dörd', 'həqiqətən', 'səhifə', 'texnologiya', 'qurum', 'beş',
              'sektor', 'geniş', 'kağız', 'ətir', 'sağalmaq', 'isti', 'əsr', 'küçə', 'bazar', 'yumuşaq', 'etmək', 'istifadə', 'sinif',
              'sevgi', 'doğulmuş', 'ağır', 'yenidən', 'günəş', 'siqaret', 'ağac', 'söz', 'bina', 'arvad', 'qaçmaq', 'partiya', 'yataq ',
              'müəllif', 'qulaq', 'müəllim', 'səbəb', 'sol', 'yaxşı', 'yağ', 'oxatan', 'başa', 'düşmək', 'gəlmək', 'gülmək', 'qayda', 'tutmaq',
              'satmaq', 'şeir', 'göndərmək', 'uğur', 'möhkəm', 'hökumət', 'ürək', 'kəsmək', 'layihə', 'lazımdır', 'sürət', 'intihar',
              'vur', 'model', 'balıq', 'şəkər', 'baxış', 'burada', 'bal', 'miqdar', 'birinci', 'kvadrat', 'ölçü',
              'seçmək', 'tətbiq', 'etmək', 'bağ', 'sevgi', 'çörək', 'boyu', 'qaçmaq', 'dolu', 'quruluş', 'demək', 'qorxu',
              'kömək', 'görüş', 'əşyalar', 'gözəlik', 'it', 'məşhur', 'böyümək', 'mənalı', 'gəzmək', 'olduqca', 'üstəlik',
              'yaşamaq', 'ağlamaq', 'istəmək', 'adam', 'çalışmaq', 'qardaş', 'çəkilmək', 'harada', 'oğurluq', 'icazə', 'qorxu',
              'işğal', 'misal', 'yalnız', 'izah', 'fikir', 'tez', 'pəncərə', 'işlə', 'daş', 'yanğın', 'fərq',
              'kifayət', 'doldurmaq', 'bəzi', 'şərt', 'qonşu', 'kişilik', 'telegram', 'istehsal', 'üstündə', 'tutmaq', 'nazik',
              'neçə', 'ümumi', 'instagram', 'şəkil', 'beri', 'dərs', 'sədr', 'qurtulmaq', 'sayı', 'dəfə',
              'olmaq', 'qərb', 'başa', 'düşmək', 'hər', 'hansı', 'sinema', 'fərqli', 'hədəf', 'yuxu', 'dost', 'fikir',
              'anlayış', 'usta', 'mətbuat', 'kənar', 'nəzarət', 'seçim', 'din', 'güclü', 'hələ', 'plan', 'beyin',
              'elektrik', 'facebook', 'şəbəkə', 'içki', 'təmin', 'edilmiş', 'oxuyan', 'xətt', 'uçmaq', 'üzv', 'dəri', 'ruh',
              'əziz', 'yanaşma', 'proses', 'baxış', 'elm', 'irəli', 'ifadə', 'bədən', 'xatırla', 'qəza',
              'hərtərəfli', 'dağ', 'yaxın', 'addım', 'ciddi', 'həll', 'impress', 'yaşayış', 'inkişaf', 'seçki',
              'ağlamaq', 'əlaqəli', 'konsert', 'artım', 'fəaliyyət', 'zərər', 'dərin', 'salon', 'mübarək', 'kəsilmiş',
              'izləmək', 'birdən', 'tutmaq', 'saymaq', 'toplamaq', 'küsmək', 'qışqırmaq', 'məsuliyyət', 'hərəkət', 'dava',
              'məktub', 'soyuq', 'canlı', 'saxlamaq', 'maşın', 'istifadə', 'köhnə', 'boş', 'görəsən', 'dərman', 'menecer',
              'qovmaq', 'metre', 'saxla', 'keyfiyyət', 'bitki', 'dəyişiklik', 'tibb', 'kredit', 'qanun', 'uğurlu',
              'bir', 'imkan', 'cəza', 'hər', 'şey', 'yardım', 'top', 'ekspert', 'doldurma', 'kanal', 'boşluq', 'uyğun',
              'illik', 'buna', 'görə', 'yazmaq', 'aid', 'olmaq', 'barmaq', 'saymaq', 'atmaq', 'müəyyən', 'etmək', 'normal', 'market',
              'prinsip', 'qırmızı', 'rol', 'mahnı', 'keyfiyətsiz', 'hazır', 'bəyən', 'nəsə', 'müəllim', 'oğlan', 'gündəlik', 'siyasət',
              'cinayət', 'niyə', 'səhnə', 'ilişmək', 'özəl', 'oturmaq', 'saxla', 'artist', 'üstünlük', 'uzanmaq', 'səhnə',
              'əlavəli', 'meşə', 'ayrı', 'sifariş', 'faiz', 'adətən', 'həmişə', 'hekayə', 'kəlimə', 'oradan', 'sizdən',
              'vergi', 'rəy', 'qardaş', 'mətbuat', 'dəstək', 'geyinmək', 'səhv', 'limit', 'birlik', 'bənövşə', 'görüşmək', 'yarım', 'yetər', 'fərdi', 'qaranlıq', 'avtobus', 'saniyə', 'körpə', 'vətəndaş', 'dövşan', 'zaman', 'millət',
              'reklam', 'yüksəlmə', 'ölçü', 'cola', 'fanta', 'sosial', 'kimsə', 'keçmiş', 'xəstəxana', 'varlıq',
              'görüş', 'jurnalist', 'daxili', 'xəbərsiz', 'keyfiyyət', 'bitdi', 'bitiş', 'yerləşin', 'giriş', 'rahat',
              'cəmi', 'birlikdə', 'mağaza', 'gizli', 'oxşar', 'dəri', 'çevirmək', 'döyüş', 'problem', 'xidmət', 'müalicə',
              'yaşıl', 'nazirlik', 'təzyiq', 'reaksiya', 'cümlə', 'istək', 'azadlıq', 'yenidən', 'şəxsiyyət', 'məsələ', 'üçüncü',
              'müəyyən', 'qiymətləndirmək', 'maraqlı', 'sürücü', 'sürətli', 'tutmaq', 'əşya', 'beynəlxalq', 'namizəd',
              'çəki', 'milyard', 'sağlam', 'sıxıntı', 'tanrı', 'rəftar', 'sosial', 'nəşriyyat', 'diqqətli', 'son', 'dərəcə',
              'topla', 'siçan', 'işıqlandırmaq', 'qarışdırmaq', 'təhlükə', 'zaman', 'dairə', 'imkan', 'informasiya', 'qarışdırmaq'
              , 'hekayə', 'tamamilə', 'təyyarə', 'cavab', 'təbiət', 'evlənmək', 'burun', 'faiz', 'əlbəttə', 'işçi', 'iş',
              'qısaca', 'mağaza', 'media', 'çünki', 'artım', 'çıxarmaq', 'ictimai', 'sığorta', 'yay', 'ürək', 'sənəd',
              'qələm', 'hər', 'gün', 'ekspress', 'risk', 'danışma', 'söz', 'demokratiya', 'duz', 'məscid', 'yaş', 'aşağı',
              'ətrafında', 'tezliklə', 'tərəvəz', 'orqan', 'öldürmək', 'başqa', 'sübut', 'qırmaq', 'baxmaq', 'meyvə', 'asmaq',
              'şirin', 'ayaq', 'dəyişiklik', 'qanun', 'külək', 'respublika', 'təkmilləşmək', 'üstün', 'yeddi', 'azalmaq',
              'qoşun', 'mobil', 'ünsiyyət', 'menecer', 'otel', 'qaçmaq', 'zövq', 'sürüş', 'təhlükəsizlik', 'qanun',
              'alətlər', 'təhlükəli', 'oxumaq', 'tüfəng', 'tələb', 'ulduz', 'intensiv', 'əsgər', 'sadə', 'qaz',
              'tətbiq', 'istehsal', 'yemək', 'dünən', 'bax', 'haqqında', 'alış', 'şüur', 'çərçivə',
              'lazımdır', 'mövcud', 'uzatmaq', 'tort', 'kino', 'qoşulmaq', 'məsələn', 'demək', 'sayt',
              'kömək', 'bacı', 'çiçək', 'hamısı', 'hörmət', 'ödəmək', 'istedad', 'ağırlıq', 'ağıl', 'çətin', 'bundan',
              'çay', 'gedər', 'müəyyən', 'zəngin', 'heç', 'söz', 'təşkilat', 'ticarət', 'boyun', 'cihaz',
              'balans', 'geriyə', 'çünki', 'qəhvə', 'əzələ', 'montaj', 'başqa', 'işləmək', 'ünvan',
              'paşa', 'istilik', 'ok', 'güvən', 'marka', 'yarpaq', 'fayda', 'yaymaq', 'axan', 'çəkmək', 'düşünmək',
              'ürək', 'arzu', 'tərəfsiz', 'şərab', 'yuxarı', 'qızıl', 'almaq', 'təmiz',
              'vitamin', 'əlavə', 'gec', 'aktyor', 'yumurta', 'hərəkət', 'kabab', 'kəsmə', 'böhran', 'şirniyyat',
              'söndürmək',
             ]


def kelime_sec():
    return random.choice(kelimeler)