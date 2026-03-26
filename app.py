from flask import Flask, render_template_string
import os

app = Flask(__name__)

profile = {
    "name": "郭人杰",
    "title": "北京大学化学与分子工程学院 博士研究生",
    "email": "2200013502@stu.pku.edu.cn",
    "office": "北京大学化学与分子工程学院 A区 611室",
    "mentor_name": "杨四海 教授",
    "mentor_url": "https://www.chem.pku.edu.cn/ktz2/wjhxktzz/150645.htm",
    "research_interests": [
        "金属有机框架材料（MOFs）",
        "多孔材料的气体吸附与分离",
        "功能配位化学",
        "环境与能源材料"
    ],
    "awards": [
        "北京大学郑格如奖学金",
        "北京大学唐仲英公益促进奖学金",
        "北京大学三好学生"
    ],
    "publications": [
        {
            "year": 2026,
            "citation": 'Liu, F.; Liang, J.; Ting, Y.; Wu, J.; Shen, Y.; <span class="author-highlight">Guo, R.</span>; Hou, Y.; Zhang, Z.; Tong, M. <i>Sunlight Triggers the Activation of Sodium Percarbonate for Toxic-Byproduct-Free Disinfection of Antibiotic-Resistant Bacteria</i>. <i>Environ. Sci. Technol.</i> 2026.',
            "doi": "10.1021/acs.est.6c00442",
            "doi_url": "https://doi.org/10.1021/acs.est.6c00442",
            "image": "Sunlight Triggers the Activation of Sodium Percarbonate for Toxic-Byproduct-Free Disinfection of Antibiotic-Resistant Bacteria.jpg"
        },
        {
            "year": 2025,
            "citation": 'Shen, Y.; Liu, F.; Liang, J.; Li, Z.; Hou, Y.; Wu, J.; Ting, Y.; <span class="author-highlight">Guo, R.</span>; Liu, Y.; Han, P.; Tong, M. <i>Activation of Chlorite with Sunlight for the Efficient Disinfection of Antibiotic-Resistant Bacteria: The Overlooked Contribution of Cytomembrane-Bound Chlorite</i>. <i>Environ. Sci. Technol.</i> 2025, <i>59</i> (36).',
            "doi": "10.1021/acs.est.5c02180",
            "doi_url": "https://doi.org/10.1021/acs.est.5c02180",
            "image": "Activation of Chlorite with Sunlight for the Efficient Disinfection of Antibiotic-Resistant Bacteria The Overlooked Contribution of Cytomembrane-Bound Chlorite.jpg"
        }
    ],
    "hobbies": [
        "篮球",
        "台球",
        "StarCraft II",
        "旅行"
    ]
}

html_template = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>{{ profile.name }} - 个人主页</title>
    <style>
        body {
            margin: 0;
            font-family: "Times New Roman", "Microsoft YaHei", serif;
            background: #f5f7fa;
            color: #222;
        }

        .navbar {
            background: linear-gradient(135deg, #8b0000, #b22222);
            padding: 0 30px;
            display: flex;
            align-items: center;
            gap: 28px;
            height: 64px;
            color: white;
            box-shadow: 0 2px 8px rgba(0,0,0,0.12);
            overflow-x: auto;
            white-space: nowrap;
        }

        .nav-item {
            cursor: pointer;
            font-size: 18px;
            padding: 8px 0;
            border-bottom: 2px solid transparent;
            flex-shrink: 0;
        }

        .nav-item:hover {
            border-bottom: 2px solid white;
        }

        .site-topbar {
            width: 82%;
            max-width: 1120px;
            margin: 24px auto 0 auto;
            display: flex;
            justify-content: flex-end;
            align-items: center;
        }

        .global-logo {
            height: 72px;
            width: auto;
            object-fit: contain;
        }

        .container {
            width: 82%;
            max-width: 1120px;
            margin: 16px auto 36px auto;
            background: white;
            box-shadow: 0 4px 20px rgba(0,0,0,0.08);
            border-radius: 14px;
            overflow: hidden;
        }

        .page {
            display: none;
            padding: 40px 48px;
        }

        .page.active {
            display: block;
        }

        .page h1 {
            margin-top: 0;
            font-size: 40px;
            color: #8b0000;
        }

        .page h2 {
            font-size: 28px;
            color: #8b0000;
            margin-top: 0;
            border-left: 5px solid #8b0000;
            padding-left: 12px;
        }

        .page h3 {
            font-size: 22px;
            color: #8b0000;
            margin-top: 28px;
            margin-bottom: 12px;
        }

        p {
            font-size: 17px;
            line-height: 1.9;
        }

        ul {
            padding-left: 22px;
        }

        li {
            margin-bottom: 10px;
            line-height: 1.8;
            font-size: 17px;
        }

        .home-grid {
            display: grid;
            grid-template-columns: 260px 1fr;
            gap: 36px;
            align-items: start;
        }

        .headshot-box {
            text-align: center;
        }

        .headshot {
            width: 220px;
            height: 280px;
            object-fit: cover;
            border-radius: 12px;
            box-shadow: 0 4px 14px rgba(0,0,0,0.16);
            border: 4px solid #fff;
            background: #eee;
        }

        .hero-title {
            font-size: 22px;
            color: #555;
            margin-top: 8px;
            margin-bottom: 18px;
        }

        .info-box {
            background: #faf7f7;
            border-left: 5px solid #8b0000;
            padding: 18px 20px;
            border-radius: 8px;
            margin: 20px 0 28px 0;
        }

        .mentor-link,
        .doi-link {
            color: #8b0000;
            text-decoration: none;
            font-weight: bold;
        }

        .mentor-link:hover,
        .doi-link:hover {
            text-decoration: underline;
        }

        .author-highlight {
            font-weight: 700;
            color: #8b0000;
        }

        .pub-preview li {
            margin-bottom: 18px;
        }

        .year-tabs {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin: 18px 0 30px 0;
        }

        .year-tab {
            background: #eeeeee;
            color: #8b0000;
            border: none;
            padding: 12px 22px;
            font-size: 18px;
            font-weight: 700;
            cursor: pointer;
        }

        .year-tab.active {
            background: #8b0000;
            color: white;
        }

        .pub-item {
            display: grid;
            grid-template-columns: 1fr 260px;
            gap: 28px;
            align-items: start;
            margin-bottom: 34px;
        }

        .pub-year-number {
            font-size: 20px;
            font-weight: 700;
            color: #8b0000;
            margin-bottom: 8px;
        }

        .pub-text {
            font-size: 17px;
            line-height: 1.85;
        }

        .pub-ga {
            width: 260px;
            height: auto;
            border: 1px solid #ddd;
            border-radius: 8px;
            background: #fafafa;
            box-shadow: 0 3px 10px rgba(0,0,0,0.08);
        }

        .footer {
            text-align: center;
            padding: 18px;
            background: #f0f0f0;
            color: #666;
            font-size: 14px;
        }

        @media (max-width: 900px) {
            .site-topbar,
            .container {
                width: 92%;
            }

            .home-grid,
            .pub-item {
                grid-template-columns: 1fr;
            }

            .headshot {
                width: 180px;
                height: 230px;
            }

            .pub-ga {
                width: 100%;
                max-width: 280px;
            }

            .site-topbar {
                justify-content: flex-start;
            }
        }
        .indent {
            text-indent: 2em;
            }
    </style>

    <script>
        function showPage(pageId) {
            const pages = document.getElementsByClassName("page");
            for (let i = 0; i < pages.length; i++) {
                pages[i].classList.remove("active");
            }
            document.getElementById(pageId).classList.add("active");
        }

        function filterPubs(year, btn) {
            const items = document.querySelectorAll("#pub .pub-item");
            const tabs = document.querySelectorAll(".year-tab");

            tabs.forEach(tab => tab.classList.remove("active"));
            btn.classList.add("active");

            items.forEach(item => {
                if (year === "all" || item.dataset.year === year) {
                    item.style.display = "grid";
                } else {
                    item.style.display = "none";
                }
            });
        }
    </script>
</head>
<body>

    <div class="navbar">
        <div class="nav-item" onclick="showPage('home')">首页</div>
        <div class="nav-item" onclick="showPage('bio')">简介</div>
        <div class="nav-item" onclick="showPage('research')">研究兴趣</div>
        <div class="nav-item" onclick="showPage('pub')">Publications</div>
        <div class="nav-item" onclick="showPage('hobby')">兴趣爱好</div>
    </div>

    <div class="site-topbar">
        <img class="global-logo" src="{{ url_for('static', filename='pku_logo.png') }}" alt="Peking University Logo">
    </div>

    <div class="container">

        <!-- 首页 -->
        <div id="home" class="page active">
            <div class="home-grid">
                <div class="headshot-box">
                    <img class="headshot" src="{{ url_for('static', filename='headshot.jpg') }}" alt="郭人杰证件照">
                </div>

                <div>
                    <h1>{{ profile.name }}</h1>
                    <div class="hero-title">{{ profile.title }}</div>

                    <div class="info-box">
                        <p><strong>邮箱：</strong>{{ profile.email }}</p>
                        <p><strong>办公室：</strong>{{ profile.office }}</p>
                        <p><strong>导师：</strong><a class="mentor-link" href="{{ profile.mentor_url }}" target="_blank">{{ profile.mentor_name }}</a></p>
                    </div>
                </div>
            </div>

            <h2>研究兴趣</h2>
            <ul>
                {% for item in profile.research_interests %}
                <li>{{ item }}</li>
                {% endfor %}
            </ul>

            <h2>获奖情况</h2>
            <ul>
                {% for item in profile.awards %}
                <li>{{ item }}</li>
                {% endfor %}
            </ul>

            <h2>Publications</h2>
            <ul class="pub-preview">
                {% for pub in profile.publications %}
                <li>
                    {{ pub.citation | safe }}<br>
                    DOI: <a class="doi-link" href="{{ pub.doi_url }}" target="_blank">{{ pub.doi }}</a>
                </li>
                {% endfor %}
            </ul>
        </div>

        <!-- 简介 -->
        <div id="bio" class="page">
            <h2>简介</h2>

            <p class="indent">
                郭人杰，2004年4月生，内蒙古自治区海拉尔人，北京大学化学与分子工程学院博士研究生。本科阶段（2022–2026）就读于北京大学环境科学与工程学院，专业方向为化学（环境化学）。

                本科期间在童美萍教授指导下开展科研训练，围绕高级氧化法水处理问题开展研究。自2025年9月起，在杨四海教授课题组开展本科毕业论文设计，研究课题为锆基金属有机框架对氨气的吸附性能调控与机理研究。

                目前研究方向主要集中于多孔材料在环境与能源领域中的应用，金属有机框架材料的结构设计及其在有毒有害气体的吸附中以及能源气体的存储中的性能调控与机理研究。
            </p>


            <h3>教育经历</h3>
            <ul>
                <li>2010-2016, 北京市房山区城关小学，小学</li>
                <li>2016-2019，北京市房山区第二中学，初中</li>
                <li>2019-2022, 北京师范大学第二附属中学，高中</li>
                <li>2022–2026，北京大学环境科学与工程学院，本科，化学（环境化学）</li>
                <li>2026–至今，北京大学化学与分子工程学院，博士，化学</li>
            </ul>

            <h3>科研经历</h3>
            <ul>
                <li>2023.10-2025.5 北京大学本科生科研项目 导师：童美萍 教授</li>
                <li>2025.9-至今 毕业论文设计  导师：杨四海 教授</li>
            </ul>

            <h3>获奖情况</h3>
            <ul>
                {% for item in profile.awards %}
                <li>{{ item }}</li>
                {% endfor %}
            </ul>
        </div>

        <!-- 研究兴趣 -->
        <div id="research" class="page">
            <h2>研究兴趣</h2>

            <ul>
                <li>金属有机框架材料（MOFs）的设计与合成</li>
                <li>多孔材料对氨气等分子的吸附与分离</li>
                <li>功能配位化学与多孔框架材料结构调控</li>
                <li>环境与能源相关材料的应用探索</li>
            </ul>
        </div>

        <!-- Publications -->
        <div id="pub" class="page">
            <h2>Publications</h2>

            <div class="year-tabs">
                <button class="year-tab active" onclick="filterPubs('all', this)">All</button>
                <button class="year-tab" onclick="filterPubs('2026', this)">2026</button>
                <button class="year-tab" onclick="filterPubs('2025', this)">2025</button>
            </div>

            {% for pub in profile.publications %}
            <div class="pub-item" data-year="{{ pub.year }}">
                <div class="pub-text">
                    <div class="pub-year-number">{{ pub.year }}</div>
                    {{ pub.citation | safe }}
                    <br><br>
                    DOI:
                    <a class="doi-link" href="{{ pub.doi_url }}" target="_blank">{{ pub.doi }}</a>
                </div>
                <div>
                    <img class="pub-ga" src="{{ url_for('static', filename=pub.image) }}" alt="Graphical abstract">
                </div>
            </div>
            {% endfor %}
        </div>

        <!-- 兴趣爱好 -->
        <div id="hobby" class="page">
            <h2>兴趣爱好</h2>
            <ul>
                {% for item in profile.hobbies %}
                <li>{{ item }}</li>
                {% endfor %}
            </ul>
        </div>

    </div>

    <div class="footer">
        © 2026 {{ profile.name }}
    </div>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html_template, profile=profile)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
