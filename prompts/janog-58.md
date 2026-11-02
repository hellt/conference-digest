>>> HOW TO RUN THIS <<<
This is the digest prompt for janog-58. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/janog-58.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/janog-58.md
Write the file into the repo directly if you can; otherwise output the
file contents so it can be saved to that path. Use that exact filename —
it is how the pipeline marks this conference done. If you wrote the file,
a brief confirmation is enough; don't also paste the whole digest.
================================================================

You are helping a product manager triage conference talks. The PM has 15+
years of experience spanning physical and software networking, network
security, and digital identity. Their core interests are: physical datacenter
networking (optics, switching, topology, RDMA/lossless fabrics, cabling,
DC/WAN interconnect), software and cloud-native networking (eBPF, Cilium,
Kubernetes networking, Gateway API, service mesh, IPAM, BGP/datapath
internals), network security, and identity/authentication (passkeys/FIDO,
OAuth, OIDC, SPIFFE/SPIRE, workload and agentic identity). Physical DC and WAN
systems work is CORE to this PM, not adjacent — do not down-rank a paper for
being about hardware, optics, or datacenter fabric.

Below is the program for JANOG 58 Meeting (operator). Read it and produce a digest
of the talks/papers/sessions most worth their attention.

## How to read this program

This is an operator program (network/infrastructure operators). Focus on
operational practice, failure stories, and techniques that transfer across
environments rather than org-specific anecdotes. Up-rank concrete postmortems,
tooling and automation that others can adopt, and hard-won lessons about
running networks at scale. Down-rank vendor-sponsored sessions that are pitches
in disguise. Note when a technique depends on a specific operator's scale or
topology.

## Enriching from the source material (best effort)

The program text gives you a title, authors, and an abstract per item, and
often links (`page:`, `pdf:`, `slides:`, `video:`). The abstract alone is thin — the full
paper has the methodology, real results, and limitations that make the What /
How / Where-applicable sections accurate instead of guessed.

If you have a tool to fetch URLs, then for EACH selected item (Core, Adjacent,
and Wildcard) try to retrieve the fuller source before writing it up:

- Prefer a `pdf:` link; else fetch the `page:` link (often has the full text or
  a longer description); a `video:` link is a last resort, don't transcribe it.
- Use what you retrieve to ground What/How/Where-applicable in the paper's
  actual contributions, evaluation, and stated constraints.

This is strictly best-effort. Many links fail or are paywalled:

- If a fetch fails, is paywalled, returns only an abstract, or you have no fetch
  tool, just fall back to the abstract already in the program text. That is
  fine and expected — do not stall or skip the item.
- NEVER invent paper contents, numbers, or findings from a failed or partial
  fetch. If you only had the abstract, write from the abstract.
- Note when an item's write-up is based only on the abstract, e.g. end its
  What line with "(from abstract only)", so the reader knows the depth.
- Do not let enrichment change which items you select or their tier; selection
  is from the program. Enrichment only deepens the write-up.

## What to produce

Group selected items into three relevance tiers:

- Core: directly relevant to the PM's core interests as listed above
  (physical DC networking, cloud-native networking, network security, or
  identity) as they work on them today.
- Adjacent: relevant to the broader field; useful context or near-term
  influence.
- Wildcard: 2-4 items that are NOT a direct fit for the PM's core interests
  but are worth their attention anyway because the work is genuinely novel or
  signals where the field is heading (a new technique, a surprising result, an
  emerging subfield). A Wildcard should make the PM think "I wouldn't have
  searched for this, but I'm glad I saw it." Do not pad this tier — if there
  are only two true wildcards, list two.

For each selected item provide, in this structure:
- **Title**: the `###` heading is the item's title exactly as the program
  gives it, with nothing added. Speaker(s)/author(s) with affiliation go on
  the line below it.
- No links section: the pipeline puts a links row (abstract page, paper,
  slides, recording) under every heading after you finish, from the program's
  `page:`/`pdf:`/`slides:`/`video:` lines and from verified sources. Do not
  write one, and do not link the title.
- **Why**: why this matters — the problem it addresses and why it's worth the
  PM's time.
- **What**: what the work actually is — the core contribution or finding, in
  plain terms (not the marketing abstract).
- **How**: how it works — the key technical approach or mechanism.
- **Where applicable**: the environment this applies to, and any specifics that
  constrain it. Explicitly flag if it is org-specific (e.g. "Alibaba-specific
  production setup", "requires Broadcom Tomahawk silicon", "assumes a
  single-operator WAN") versus broadly applicable. If it's a general technique,
  say so.

Then a short "Themes" section (3-6 bullets) naming patterns across the
program: what the field is collectively paying attention to this cycle.

## Rules

- Prioritize ruthlessly. 15 sharp picks beat 60 hedged ones. A large program
  should still yield a tight list.
- Skip pure product pitches, sponsor slots with no substance, and
  beginner/101 sessions unless they signal a real shift.
- If the program text is incomplete or an abstract is missing, say so for that
  item rather than inventing content.
- Do not invent talks, authors, or affiliations. Use only what's in the
  program text below.

## Output format

The digest is read on GitHub (GitHub-Flavored Markdown viewed in the repo) and
on the project's Zensical site, which renders the same file. Use only syntax
both render reliably, and follow these rules:

- Headings with `#`/`##`/`###`; bold with `**...**`; italics with `*...*`.
- Bullet lists with `-`. Put a blank line before every list, before every
  heading, and between paragraphs, or they won't render correctly.
- Indent nested lists by four spaces per level; avoid deeper nesting.
- Any link you do write is `[text](url)` — never a bare URL — and uses a URL
  exactly as the program text gives it.
- No raw HTML except the metadata comment below. Do not use heading IDs,
  footnotes, definition lists, or other non-GFM extensions.
- You may use tables and `code spans` where they genuinely help, since GitHub
  supports them; don't force them.

Begin the output with this metadata, wrapped in an HTML comment so it does not
show in the rendered view but stays in the source:

<!--
conference: JANOG 58 Meeting
type: operator
source_url: https://www.janog.gr.jp/meeting/janog58/program-timetable/
generated: 2026-11-01
registry_key: janog-58
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

### 新人のためのインターネット&ネットワーク超入門 2026
video: https://youtube.com/live/RW42o2yGoUc | slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/janog58-pr-tutorial-TaijiTsuchiya.pdf
「インターネットの中身」についてどれぐらい知っているでしょうか。 普段から当たり前のように使われているインターネットですが、その裏側の仕組みや業界構造まで知っている人は決して多くはありません。 本講演では、現役ネットワークエンジニアでありYouTubeで7年以上に渡って情報発信してきた発表者が、業界関係者しか知らない「インターネットの裏側の仕組み」について、実例を出しながらなるべく具体的に、かつ新人の方にもわかりやすいように噛み砕いて解説します。 インターネットの全体像を掴むことで、インターネットを構成する各企業の存在や役割を正しく理解し、今後インターネット業界で働く上で本質的な課題解決・企画制作・サービス提案の助けになります。 本講演で扱う内容 インターネットの中身を覗いてみよう – 家の中のネットワーク – アクセスネットワーク – ISPネットワーク – 相互接続 / IX / ピアリング – とう道 / 海底ケーブル インターネットを構成する組織を覗いてみよう – ISP / CATV / モバイル事業者 – アクセスネットワーク事業者 – IX / トランジット事業者 – DC事業者 / クラウド事業者 / CDN – コンテンツ事業者 インターネットトラフィックを覗いてみよう – 通常時のトラフィック – 人気イベント時のトラフィック – 障害発生時のトラフィック 本講演で扱わない内容 – ルーター・サーバー等の具体的なコマンドや設定方法 – 各技術の詳細な解説 本講演にぜひ参加していただきたい方 – 新たにIT企業・ネットワーク企業に就職された方 (職種・年齢は問いません) – 新たにエンジニア部門に配属された新人エンジニアの方 – 自身にインターネットの知識を取り込みたい方 注意事項 本講演は、JANOG58会場での現地講演と、YouTube Liveによるオンライン生配信(アーカイブ予定)を同時並行で実施します。みなさまのご都合に合わせて、現地参加 or YouTube Live視聴をご検討ください。 YouTube Live は 以下のURLで10:20頃から配信予定です。 https://youtube.com/live/RW42o2yGoUc 上記のURLで繋がらないようであれば show int チャンネルページ ( https://www.youtube.com/@showint ) からリンクを探してください。 受講終了後は、以下の事後アンケートのご協力おねがいします。今後の取り組みの検討材料にさせて頂きます。 https://forms.gle/rrESytN99rEVpEMaA

### JANOG58スタートガイドLT
slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/07/J58_pd_concept_tominaga.pdf | slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/07/janog58-pd-concept-khyodo-00.pdf | slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/07/janog58-pd-concept-nkamitani-01.pdf | slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/janog58-pd-concept-shtsuchi-00.pdf
JANOG57で大好評だった「スタートアップガイドLT」を、JANOG58でも開催します！ 今回は開会宣言前の特別プログラムとして実施。JANOG58を最大限楽しめる内容になっています。 初めて参加される方にはもちろん、これまで参加経験のある方にも、 JANOG58ならではの魅力や楽しみ方をぎゅっと凝縮してお届け！ もっと深く、もっと楽しくするヒントが満載です。ぜひお気軽にご参加ください！ 内容 タイトル 所属or役割 登壇者 資料 スタートガイドLTとは？ JANOG58プログラム委員 冨永 良明 公開資料 JANOG58のこだわり1 アリスタネットワークスジャパン合同会社 兵頭 弘一 公開資料 JANOG58のこだわり2 アリスタネットワークスジャパン合同会社 神谷 尚秀 公開資料 JANOG58のこだわり3 アリスタネットワークスジャパン合同会社 土屋 師子生 公開資料 JANOG58を楽しむための用語集 株式会社MIXI F5ネットワークスジャパン合同会社 相原 一輝 鈴木 章 公開資料 みんな知りたい愛媛県県民文化会館 長崎県立大学 山本 くるみ 公開資料 ブースラリー参加しませんか？ 近畿大学大学院 温井 直輝 公開資料 お楽しみ企画について シスコシステムズ合同会社 嶋 勝也 公開資料

### 野良BoFフラッシュ
JANOG では、参加者のみなさんが気軽に集まって話したり、好きなテーマで議論したりできる BoF（Birds of a Feather）という場があります。 今回の JANOG58 でも、前回に続き初日のセッションが始まる前に「野良BoF紹介タイム」を設けることになりました。 この時間では、野良BoFの主催者の希望者のみなさんに、記入いただいたタイトル・主催者名・内容の概要・開催日時・ひとことコメントをまとめたスライドを使って、順番に紹介していきます。 「どんなBoFがあるのかな？」と気軽に眺めてもらえる時間です。 “参加したい！”と思えるBoFを見つけるため是非ご参加ください！ 以下のGoogleスライドに記載頂き、順に発表を行っていただきます。 テンプレートをコピーし、主催BoFのスライドを追加してください。 当日はスライドに記載の順で発表していただきます。時間になりましたら開催

### JANOGの歩き方
slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/07/JANOGの歩き方_JANOG58.pdf
JANOGミーティング開始直前に、JANOG自体についての説明、およびJANOGの活動内容を紹介するセッションを設けます。 主にJANOG初参加の方、JANOGについて詳しくない方への説明内容となっておりますが、どなたでもご参加いただけます。 また、説明終了後には参加者同士の交流の時間をご用意いたします。 座席はランダムとしていますので、JANOGer同士での交流をお楽しみください。

### 開会宣言
slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/07/JANOG58_kaikai_sengen.pdf
開会宣言

### 「生成AIを用いたネットワーク監視」の実運用課題と利用コスト～そのLLM、いくらかかってますか？～
slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/janog58-pr-genai-nw-monitoring-高野-悠生-レヌグンタ-タンマイ_講演資料_修正.pdf
生成 AI を用いたネットワークオペレーション改善・効率化は、 実運用への本格導入が進む重要な技術トレンドです。 LLM 適用の効果は JANOG でも多くの発表がされております。 その有用性が確立される一方で、LLM を利用するための実課題・運用コストについてはまだあまり見えてきません。 NTT-AT ではLLMを用いたSyslog・パケット解析システムをサービス化し、各社様に導入を進めております。 上記内容を弊社サービスとして運用した際の「LLM利用オペレーションの実運用課題・実コスト」について、 実例を中心にご紹介させていただきます。 また実際に、今年度の大規模ネットワークでの実証実験結果を元にして、 ・どの程度の利用コストが発生し ・どのような方式でコスト改善効果が見られたか といった内容についても、ご紹介させていただきます。 「どのような利用ケースで」「どの程度のコストがかかり」「どう改善したのか」といった、 今後のネットワークオペレーションの一助となるナレッジを、皆様に共有できればと思います。 議論ポイント LLMを活用したNWオペレーションの事例・実例をご紹介しつつ、 JANOGの皆様と、実運用での課題や改善方法について、議論できればと考えております。 特に、LLMの長期的な運用コストや、持続的な改善方法について、 実証実験の内容を踏まえながら、今後のナレッジに繋がる議論をさせて頂きたいです。 [議論ポイント] ・LLM利用の実運用で、困りごとはないか ・LLMオペレーションのイニシャルコストをどう考えるか ・許容できる「利用コスト」と改善方法について ・運用環境のアップデート方法 プログラムで扱う内容について LLMオペレーションの実サービスや大規模ネットワークの実証で得られたナレッジを元に、 お時間の許す限り、以下のトピックをご紹介させていただければと思います。 (1)LLMを用いたネットワーク・ログ監視における実運用構成 ①Agentic AIによるイベントドリブン型トラブルシューティング ②MCPプロトコルによるネットワーク情報との連動 (2)LLMを用いたネットワーク・ログ解析の運用事例と課題 ① NWデータRAGが”大きすぎる/多すぎる” ② オペレータのAIリテラシにどう追従するか ③ 大規模NWにおけるLLMオペレーションの「実利用コスト・利用トークン」と改善手法 ④ 分析サービスとして提供した際の想定コストと実体 (3)LLMオペレーションのコストを考える ①LLM利用におけるイニシャルコスト・ランニングコストとは ②「費用」ではないコストも無視できない ③プロプライエタリモデルからオープンモデルへの代替可能性

### CLIパーサーからの脱却 – モデル駆動型プラットフォームによるマルチベンダー検証の完全自動化
slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/janog58-pr-cli-parser-ohihara-yokoyama.pdf | slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/07/janog58-pr-cli-parser-OhiharaYokoyama.pdf
JANOG54では、OpenConfigと検証フレームワークONDATRAを活用したNW検証自動化の挑戦と課題を共有しました。今回の発表では、その後の大規模な実業務展開で浮き彫りになった課題と、それを克服するための我々の新たな取り組みについて共有します。 KDDIのネットワーク検証業務では、マルチベンダー構成かつ数千項目に及ぶ膨大な検証項目への対応が求められます。この要求に対し、従来の「属人的なスクリプト管理」は限界を迎え、「組織的なプラットフォーム運用」への転換が不可欠となっていました。我々はこの課題を解決するため、YANGモデル（OpenConfig/Vendor Native）とOpenConfigベースの検証フレームワークONDATRAを拡張した、独自の検証プラットフォームを内製開発しました。 このプラットフォームを大規模な商用導入検証に実戦投入した結果、従来は数ヶ月を要していた検証期間をわずか数日へと劇的に短縮し、マルチベンダー環境における検証のスケールアウトを実現しました。 本セッションでは、自動化を大規模展開するにあたり直面した以下の課題に対し、ソフトウェアデザインとプラットフォーム化によっていかにして乗り越えたか、その具体的な知見を共有します。 ・マルチベンダー対応によるコードの肥大化 ・CLIパーサーのメンテナンス問題 ・自動化コードの実行性と再利用性の欠如 さらに、技術的ポイントとして、以下の詳細にも踏み込みます。 ・ygot/ygnmiを用いたYANGモデルベース開発による「CLIパーサーからの脱却」 ・OpenConfigのカバレッジ不足を補完する、Vendor NativeやCLIを併用したハイブリッド戦略 ・自動化の高度化に伴う「スキルセットの増大」を解消するための抽象化の工夫 ・ベンダー間の実装差異を管理し、環境依存の設定を分離するアーキテクチャ 単なるツール紹介に留まらず、自動化を「持続可能な組織の資産」にするための設計思想を共有し、NWエンジニアにとってより良い自動化のあり方を皆様と議論したいと思います。 議論ポイント NW検証の実施項目について ・どのようなプロセスや考え方で検証業務を定義し実施していますか？ ・検証業務の組織間での共通化や外部化についてどう考えますか？ - Google の Feature Profiles(*) や、検証コードの機器ベンダーとの共有など NW自動化の組織的アプローチについて ・自動化における3つのロール（要件定義、開発/保守、利用/実行）をチームとしてどう分業・連携させていますか？ - 「分業によるコミュニケーションやスキルギャップの壁」を乗り越える工夫はありますか？ ・自動化人材の育成において、「NWエンジニアへのSW教育」と「SWエンジニアへのNW教育」のどちらが近道でしょうか？ - 生成AIやコーディングエージェントの普及は、このどちらの学習コストをより引き下げていると感じますか？ NW自動化のソフトウェアアプローチについて ・CLIパーサーベースの自動化/コードベースでどのような課題を持っていますか？ ・マルチベンダー検証の自動化において、ベンダー間の差異をどのように管理していますか？ ・モデルベースのAPIやインターフェースを持つネットワーク機器が増えてきている中で、どこまでこれを実運用し始めていますか？ (*) NW機器の挙動を検証するためのテストスイート（ONDATRAテスト群）を定義・提供するリポジトリ https://github.com/openconfig/featureprofiles プログラムで扱う内容について プログラムで扱う内容 ・開発したマルチベンダー対応のテストフレームワークのデザインや概要 ・OpenConfig/YANGベースのテストフレームワークONDATRAの使い方 ・OpenConfigと既存手法(CLI/Vendor Native)の組み合わせや両立方法 ・大規模なテストシナリオのコード開発と運用における保守性やスケーラビリティ上の課題と対策 プログラムで扱わない内容 ・コーディングにおけるAIの活用方法について ・具体的な検証業務の項目やクライテリアについて

### プライベートクラウドを”継承”する ― Cycloudのネットワークを全面刷新した話
slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/janog58-pr-private-cloud-koshouji-00.pdf
我々が所属するCIU (CyberAgent group Infrastructure Unit) は、サイバーエージェント社内にプライベートクラウド「Cycloud」を約20年にわたり運用・提供してきました。 長い歴史を持つCycloudですが、長期運用を続けていく中で以下のような課題がありました。 – パブリッククラウドに慣れたユーザーにとって非直感的な仕様 – 数年に一度のDC・VM基盤移行 / 定期的メンテナンス時のVM移設作業 – 特有のネットワーク仕様 – VRF / Subnetが手動デプロイでスピード感に欠ける – LBのソースIP維持の設定が複雑(DSR/Proxy Protocol) – VRFでのネットワーク分離が完璧ではない – ネットワークがスケーラブルではないこと – VRF境界のFirewallの輻輳 – 拠点間接続のコストパフォーマンスが悪いこと これらの課題を解消するために2024年頃より刷新計画を進め、晴れて2026年4月に新リージョンの提供を開始しました。 本セッションでは、これらの課題にどのように対応し、どのような苦労があったかを共有します。 そのうえで、国内でも数少なくなったプライベートクラウドがこの先どのように成長・継承していけばよいのか、会場の皆さんと議論したいと思っています。 議論ポイント ■ テクニカル – EVPN/VXLANファブリックについて – EVPN Route Type 5 についての知見・苦労話 – マルチベンダーでの EVPN/VXLAN 環境の事例はありますか – 負荷試験はどうしていますか – ファブリックの監視はどうしていますか – 拠点間接続での波長貸しサービス / 400G-ZR 導入について – DSR廃止後のLBアーキテクチャ（N+1構成など）についての知見 – マルチテナント環境における Firewall の在り方をどう考えるか – NW刷新に伴う検証環境はどのように準備していますか ■ 組織・運用 – ネットワーク以外のチーム（サーバー基盤・アプリケーション等）との連携について – 責任分界点の決め方（例: MetalLB等サーバーサイドでBGPを扱う場合の棲み分け） – プライベートクラウドとパブリッククラウドの棲み分けについてどう考えますか – プライベートクラウドやネットワーク刷新を経験した方の苦労話・知見の共有 – NW刷新プロジェクトにおけるCoding Agent / AIの活用について

### 井戸端オープンマイク ゆる〜く話そうJANOGの未来
slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/井戸端オープンマイク-ゆる〜く話そうJANOGの未来.pdf
「大きな会場では少し話しにくい」「オープンマイクで話しきれなかった」「JANOGについてもう少し話したい」 そんな思いを持っている方も、愛媛の風に吹かれながら、肩の力を抜いてJANOGのこれからについてゆる〜く話してみませんか。 JANOGをより良くしたいという思いが集まる場として、オープンマイクは大切な役割を持っています。 近年のオープンマイクでも、JANOGに関するさまざまな意見や問題提起が交わされ、議論が白熱する場面が見られます。 一方で、大きな会場や限られた時間の中では、うまく話せなかったこと、発言しづらかったこと、もう少し掘り下げたかったこともあるのではないでしょうか。 会則を定めるJANOG Comment 2では、オープンマイクについて次のように定められています。 第5章 オープンマイク 第14条（機能と運営） 1 運営委員会は、本会の運営に関して会員および本会の関係者と広く意見を交換するため、ミーティングの開催に合わせてオープンマイクを開催する。 2 オープンマイクは、年1回以上開催するものとする。 本プログラムでは、通常のオープンマイクで出た話題や、そこで十分に話しきれなかったテーマを起点に、参加者とコミッティメンバーがJANOGそのものについて意見を交わします。 会場の距離の近さを活かし、参加者が自分の関心に応じて、気軽に話せる時間を目指します。 話題としては、参加者が増える中での課題、初参加者も含めた参加しやすさ、BoFやメーリングリスト、JCなど、JANOGに関するさまざまな論点を、必要に応じて取り上げます。 こんな方の参加をお待ちしています。 ・前回のオープンマイクで発言できなかった方 ・今後のJANOGについて、アイディアをお持ちの方 ・JANOGについて一言言いたい方 ・JANOGに参加するのが楽しい方 ・JANOGに初めて参加した方 ここで交わされた意見や話題は、DAY3のオープンマイクの参考としても扱われます。 ただし、本プログラムで話した内容について、DAY3のオープンマイクで改めて発言することを求めるものではありません。 JANOGのことを少しでも話してみたい方、聞いてみたい方、考えてみたい方が、気軽に参加できる場にできればと思います。

### ネットワーク監視の自動化はどこまでできるのか? -Apache Airflowによるアラート対応基盤-
slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/janog58-pr-auto-nw-monitoring-HonaiUeoka.pdf
LINEヤフーのデータセンタネットワークでは、24/365の常駐人員による監視を前提にした運用を行っていました。 しかし、対応の手順書が整備され「成熟」していても、その実行主体が人である限り、運用負荷、改善速度などの運用の「継承」に限界があります。 今回、弊社では、アラート対応を人手によるものから基盤が自動実行し必要な時だけ人に渡す運用へ切り替える取り組みを行いました。 アラートを受けて処理を自動実行する基盤を、OSSのワークフローランナーであるApache Airflowを中心に整備しました。 ワークフローと実行履歴が可視化されることで、失敗時の追跡や人手介入がしやすくなり、自動化をブラックボックス化させずに運用することができます。 この基盤を使い、複数チームのアラート一次対応を自動化することができました。 本発表では、人手による対応の課題、アラート対応基盤の実装、それを複数チームで使える形へ整え、実運用へ適用する過程で得られた知見を共有します。 アラート対応を自動化することはどこまで実現可能なのか、そこにどのような壁があるのか、自動化が進んだ先の課題について参加者のみなさんと議論したいと考えています。 議論ポイント – NWアラート対応は人手が担っていますか。どれくらい自動化されていますか。自動化するハードルはどこにありますか。 – ワークフローランナーのApache AirflowをNW運用に使うことに関してどう感じますか。 – 共通の運用基盤を、実際に運用チームに使ってもらうには、どのようなハードルがありますか。 – NW運用の自動化が進む（成熟する）ことで、NW運用の知識・知見が継承されにくくなるのをどう防ぎますか。

### データセンター構築・移設のリアル​〜国内外の事例から考えるスムーズな進め方〜​
slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/07/pr-dc-build-move-tomoyatakezaki_public.pdf
データセンターへの設備構築や移設の現場では、十分な事前計画を行っていても、環境差分や調整不足、想定外の制約によって作業が計画通りに進まないことが多くあります。本発表では、IIJにおける国内外のデータセンター設備構築・設備更改・移設の実例をもとに、実際に発生したトラブルや作業遅延要因を振り返ります。具体的には、海外を含む複数拠点での構築・移設作業において顕在化した課題や対応を紹介し、

### 国内でCDN作ってる人集まれ！〜国内のCDN事業者の実際の話〜
slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/07/pr-cdn-japan_takamizawa_pre.pdf | slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/07/pr-cdn-japan_takamizawa_after.pdf | slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/07/pr-cdn-japan_oka_after.pdf | slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/07/pr-cdn-japan_ogawa_after.pdf
CDNが配信するトラヒックは70%を超えているという試算もあり、インターネットの上で重要なインフラとなっています。一方でCDNはニッチな分野となっており、仕組みや実際の運用について国内で議論される場面は少ないのが現状です。 本発表では、国内でCDNを実際につくっている方々に集まっていただき、各社のCDNの成り立ちや特徴、システム構成について紹介いただきます。また、CDNのコア技術であるキャッシュについてやAIによって変わるCDN、ハイパースケーラーと国内CDN事業者の共存などのテーマでパネルディスカッション形式で会場の皆様からもコメントをいただきながら、今後のCDNのあり方について議論させていただければと思います。 そしてJANOG58のテーマである「技術の成熟と次代への継承」。このディスカッションでは、CDNを作っていく中での楽しみやワクワク感を少しでも若手エンジニアの方々に届けられればと思います。 議論ポイント ・CDNの中身や仕組みについての説明を通して、日頃の疑問や突っ込み、コメントなど ・CDNはAIやLLMへの対応が必要になっているが、ネットワーク側はどう変わったのか？ ・またどのように対処するべきなのか？活用という側面ではなく実サービスへの影響や対処という側面で議論したい ・海外事業者と国内事業者での役割分担は可能か？可能であればどういう分担が理想か？ ・安全保障観点での国内CDN事業者の必要性 ・CDN事業者とネットワーク事業者の楽しみの違いや苦労の違い ・CDN作ってみたいですか？（若手の方々からの意見をいただけるとうれしい）

### あのネットワーク技術の今と予想する10年後
slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/Observability-Telemetry-（安藤）.pdf | slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/PQC-（高橋）.pdf | slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/Media-over-IP-PTP（北島）.pdf
ネットワーク技術は、一度広く使われ始めると長く残り続ける一方で、その役割や使われ方は少しずつ変化していきます。 本プログラムでは、「あのネットワーク技術の今と予想する10年後」をテーマに、現在注目されている技術や、今後ネットワーク運用に影響を与えそうな技術について議論します。 扱うテーマは、Observability / Telemetry、Media over IP / PTP、PQC の3つです。 SNMP中心の監視からTelemetryを活用した可視化へ、専用的な映像伝送技術からIPネットワーク上でのリアルタイム伝送へ、そしてポスト量子暗号への移行がネットワーク機器・認証・制御プレーンに与える影響へと、それぞれ異なる分野からネットワークのこれからを考えます。 各テーマでは、現在どのように使われているのか、現場では何が課題になっているのか、10年後にはどのような姿になっているのかを、登壇者の経験や視点を交えながら掘り下げます。 単に「新しい技術が来る」「古い技術がなくなる」といった話ではなく、既存技術の役割がどう変わるのか、ネットワーク運用者は何を意識しておくべきなのかを議論する場にしたいと考えています。 参加者にとって、普段触れているネットワーク技術を少し先の未来から見直し、これからの学び方や運用の考え方を持ち帰るきっかけとなることを目指します。

### Agent skillsとMCP Appsを活用した伴走型AIOpsについて
slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/janog58-pr-collaborative-aiops-佐藤亮介-.pdf
マルチエージェントやMCPによって、オペレーション業務支援に特化したchatbot等が作成可能になり,これまでのJANOGでも多くのエージェントが提案されてきました。 一方、複数エージェントの個別チューニングによる開発負担や、 NW状況の理解や指示がチャット（テキスト）ベースだと非効率でオペレータに負荷がかかる等の課題があります。 本発表では、新しく登場したチューニング方式のAgent Skillsや状況に応じたGUIを動的に生成しオペレータと会話できるMCP Appsによって、容易に様々な故障対応ノウハウをチューニングできユーザフレンドリなGUIを用いてオペレータの状況に寄り添った支援が可能な伴走型AIOpsについてご紹介します。 議論ポイント AIエージェントをNW運用業務にどのように活用していますか？ AIチャットに取り込みたい運用ツールのGUIはどのようなものがありますか？など プログラムで扱う内容について TBA

### 巨人が育てた好敵手達〜 競争と訴訟、そして知財が導いた進化論 〜
皆さんが普段運用の為に使用しているネットワーク機器のCLIはどの様に生まれ、広く使われてきたのでしょうか。 本発表では業界の覇権を握る絶対的な巨人とそれに挑んだ好敵手の間で繰り広げられた知的財産(特許や著作権）を巡る熾烈な闘争の歴史を共有します。 市場を先導するトップ企業は自社の技術と顧客を守る為に、特許という強力な武器で行くてを阻もうとします。 挑戦者達は法的な制約を回避する為にソフトウェアのアーキテクチャーを根本から見直し、再設計を行う事でその業界にはより良い選択肢が生まれる事となります。 今回のJANOG58のテーマは「技術の成熟と次代への継承」です。 2003年/2014年におこなれたネットワーク機器の訴訟事件を皆さんに共有する事で、エンジニアが知っておくべき知的財産の考え方を議論する事が出来ればと思っています。 議論ポイント 様々な論争のユースケースを共有する事で、自分達の経験も共有できやすくなるのではないか思ってます。 プログラムで扱う内容について 控訴内容など公式発表に基づいた事実のみを共有します。 知財の概要に関してはご説明しますが法律詳細など解釈しきれていない部分はありますのでご了承下さい。

### プラットフォームにおける組織間対話の重要性 – 実例から見るNWにおけるソフトウェア運用 –
slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/07/J58_pr-platform-dialogue.pdf
プラットフォーム運用における組織間の対話や交流の大切さを議論したい JANOG57 にて、ネットワークエンジニアとプラットフォームエンジニア（k8s 等の基盤エンジニア）との対話に関する発表がありました。 ( 今こそ学びたいKubernetesネットワーク ～CNIが繋ぐNWとプラットフォームの「フラッと」な対話 ) CNI という技術カットで、組織間の技術交流の重要性について提起した発表だと思っています。弊社は Neco というプラットフォームを運用しており、組織間対話の重要性を多方面で感じています。一つのアンサーソングとして、今回は「プラットフォーム運用」というカットで、組織間対話についての弊社の経験や考え、悩みをお伝えしたいと思っています。 AI 時代、運用が大きく変わっていく中で、皆様から幅広い議論をお願いしたいと思っています。 議論ポイント 深い専門性が求められる中で、知識の幅も重要であり、その掛け算になる運用組織は組織間の対話によって成熟させていかなくてはならないと考えています。サイボウズにおける事例をご紹介しながら、皆さんと成熟した組織を次に継承していくために必要なものは何か、技術的な面、組織的な面、両方の観点から議論し、有益な知見を育てていきたいと考えています。

### JANOGerのみなさん！地域NOGに参加してみませんか？
現在、国内では6つの地域NOGが活動しています。JANOGと地域NOGは相互に協力や補完する関係性を持ち合わせています。JANOGには参加しているが、地域NOGを知らなかった方、知っていても、どのような活動内容かは知らない方、参加したことがない方、地域NOGに興味がある方へ向けて、各地域NOGのコアメンバーから活動状況報告や次回開催紹介を行い、地域NOGの活性化に繋がる議論を行いたいと思います。 プログラムで扱う内容について -各地域NOGの紹介、活動報告、次回予告 -地域NOGに関連するディスカッション

### そのトラフィックは誰のため？ 生成AIがもたらす「AI-to-AI」通信時代のNWデザイン
slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/janog58-pr-traffic-for-whom-KanameNishizuka.pdf
生成AIの普及により、GPUクラスタを中心としたDC内ネットワーク技術や電力消費への注目は急速に高まっている。一方で、生成AIがインターネットトラフィックにどのような影響を与えているかについては、まだ十分に議論されていない。 本発表ではまず、データ収集・学習・推論それぞれのフェーズにおいて、どのようなトラフィックがDC内/DC間/インターネット上を流れるのかを整理する。さらに、学習時の集中型トラフィックに加え、推論処理に伴う継続的・分散的な通信需要の増加を踏まえ、今後どのような通信パターンが増加していくのかを考察する。 その上で、人間の認知帯域がボトルネックとなる現状や、AI-to-AI通信の増加によって変化するラストワンマイルの役割を整理し、AI時代にネットワークオペレーターが注視すべきポイントについて議論する。 議論ポイント ・AIトラフィックの主戦場は依然としてDC内/DC間？ ・人間が生み出すトラフィックはそろそろ頭打ち？ ・ラストワンマイルには今度どのようなトラフィックが流れる？ ・AI時代のトラフィック最適化は？

### ベテランエンジニアの「勘」はLLMに移植できるのか RAGで再現できるもの・できないもの
slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/janog58-pr-engineer-intuition-llm-石井秀和-春原寿里r2.pdf
・ベテランエンジニアの暗黙知の本質は、特定システムの障害事例の記憶ではなく、複数のシステム・構成・障害を渡り歩く中で形成された「システムはこの条件が揃うとこう壊れる」「この挙動はこのレイヤが怪しい」という抽象化された判断モデルだと考える。 ・実際に自社でKnowledge Baseを構築・運用した経験から、文書化された知識はRAGで再現できた一方、この「抽象化された経験モデル」はRAGでは再現できなかった実例を報告する。どのようにすればこの抽象化モデルを実現できるか参加者と議論する。 議論ポイント ・「ベテランエンジニアっぽいLLM」を作るとしたら、どのアプローチが現実的か？ ・ベテランが現役のうちにできることはなにか？ プログラムで扱う内容について TBA

### 耐量子計算機暗号への移行準備してますか？ ～2030年台の安全なネットワークに向けて～
slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/JANOG58_耐量子計算機暗号への移行_事前資料.pdf
量子計算機の進展により現行公開鍵暗号の危殆化が現実味を帯びる中、耐量子計算機暗号（PQC）への移行が世界的に加速している。 本発表では、PQCを巡る最新の国際・国内動向を整理するとともに、インターネットルーティング分野（BGP/RPKI/DNSSEC）におけるPQC移行の現状と課題を概観する。 あわせて、パナソニックにおけるIoT機器およびBGPsecへのPQC部分導入に関する具体的な実装・評価事例を紹介する。 議論ポイント PQCの認知度や2035年までの移行目標に対する理解状況を参加者間で共有し、ネットワーク事業者における現在の取組状況を可視化する。 あわせて、PQC移行に着手できていない背景や、技術的・運用的な障壁（パケットサイズ増大、処理性能、段階導入の難しさ等）を整理する。 これらを踏まえ、ネットワーク業界として現実的なPQC移行タイムラインや優先度付けについて議論する。

### 初心者LT
slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/目的から紐解く！DCNWとAINWの3つの違い_別所優音-1.pdf | slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/ShowNet2026での-デジタルツインの取り組みと得られた知見_森本虎南.pdf | slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/「ルーティング技術」で勘違いした事例共有_船岡聖矢-2.pdf | slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/ネットワーク分析で「読むべきRFC」を探す_外山結月.pdf.pdf
開催概要 採用プログラム一覧 採用プログラム詳細 初心者視点で整理するDCNWとAINW – 目的から紐解く3つの違い- 発表者 アブストラクト 応募資料 採点結果 ShowNet2026での デジタルツインの取り組みと得られた知見 発表者 アブストラクト 応募資料 採点結果 「ルーティング技術」で勘違いした事例共有 発表者 アブストラクト 応募資料 採点結果 ネットワーク分析で「読むべきRFC」を探す 発表者 アブストラクト 応募資料 採点結果 専用線系サービスのテクニカルサポート紹介 発表者 アブストラクト 応募資料 採点結果 WireGuardで始めるVPNパケットキャプチャ入門 発表者 アブストラクト 応募資料 採点結果 AWS初心者がハマった5Gコアのパブクラ適用における経路切替の落とし穴 発表者 アブストラクト 応募資料 採点結果 V2X通信のポテンシャル評価 発表者 アブストラクト 応募資料 採点結果 LTプログラム募集について 募集期間 応募方法 選考方法 審査員 留意事項 よくある質問

### 爆発するMACアドレスとの戦い EVPN VESPA/仮想イーサネットセグメントとProxy ARPの活用
slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/06/janog58-pr-mac-address-explosion-tsuchiya-00.pdf | slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/janog58-pr-mac-address-explosion-kawakami-yamamoto-00.pdf
データセンタービジネスが立ち上がってきた2011年。 データセンターのネットワークでは仮想マシンの普及により、大量のMACアドレスと モビリティ提供の為のレイヤー２の拡張のため、不安定なネットワークを構築しなければいけませんでした。 BGPを使ったネットワークデザイン IP ClosやVXLANの登場により、安定したネットワークとモビリティを同時に実現する事が出来るようになりました。 15年経った2026年、我々はまた新しい問題に直面しつつあります。 ムーアの法則により高密度収容できるようになったCPUやメモリと変わらない仮想マシンのサービス仕様やK8sでのコンテナの活用が増えてきた事によりデータセンターのMACアドレスはまた増えており、各企業のネットワークではBYOD/IOTデバイスの普及やMACアドレスのランダム化によりさらなるMACアドレスへの対応が必要になっております。 本プログラムではEVPNを使ったVESPA(Virtual Ethernet Segment with Proxy Arp)を紹介する事で現在抱えてる問題点を認識し、様々な運用者の方々と議論が出来れば良いと思っています。 議論ポイント 実際にMACアドレスの増加などで困ってるデータセンター運用者や企業のネットワーク管理者がいるのかどうか、またL2 Proxyをなにかで既に実現してる人がいれば是非聞いてみたい

### RPKIキャッシュサーバの課題と提案 -より信頼できるRPKIを目指して-
slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/RPKIキャッシュサーバの課題と提案-より信頼できるRPKIを目指して_山口勝司-2.pdf | slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/RPKIキャッシュサーバの課題と提案-より信頼できるRPKIを目指して_後藤汰珠.pdf
BGPルーティングセキュリティの分野において、RPKI/ROVはここ数年で急速に実用段階へと移行した。日本国内におけるROV導入率（INVALID経路の破棄率）は2026年現在で約40％に達しており、2024年以降はJPNICによるガイドライン公開などを契機として普及が加速している。AS間の相互接続においてもROV実施が推奨される場面が増え、ROVへの対応は事実上の標準として定着しつつある。技術の成熟という観点から見れば、ROVはすでに「導入するかどうか」の議論を超え、「いかに安定・信頼性高く運用するか」という段階に入っている。 一方、ROVの仕組み上、RPKIキャッシュサーバがリポジトリからRsyncまたはRRDP経由でROA情報を収集し、生成したVRPをBGPルータに配布するという構造を持つため、リポジトリとの通信障害やリポジトリ側のトラブルによってVRPが不完全な状態となった場合、不正な経路の流入を防げなくなるリスクが存在する。また、ROA作成者の設定誤りによって正当な経路がINVALIDと誤判定され、意図しない通信障害を招く可能性もある。 ビッグローブと長崎県立大学は、ルーティングセキュリティに関する共同研究の中でこの課題に着目し、「VRPブレーカー（特許出願中）」を開発した。本機構は、リポジトリから取得したROA情報をルータへ反映する前に検証を行い、異常の可能性が検出された場合にVRPの配布を一時停止することで、不完全なVRPに起因するリスクを低減するものである。 本プログラムは、ROVが成熟技術として広く普及していく過程で顕在化してきた運用上の課題を整理したうえで、VRPブレーカーの設計と動作について説明する。また、RPKIの信頼性をさらに高め、次世代の運用者へ安定した技術基盤を引き継いでいくために、インターネットコミュニティとして何に取り組むべきかを参加者とともに議論したい。 議論ポイント ■ROVのリスクに関してどう考えていますか？ ・ROVのリスク（不完全なVRPによりINVALID経路がFIBに乗る可能性）とその対策について ・正常な経路がROVにより破棄されて通信障害となるリスクについて ・「NOTFOUND」の経路を破棄(または優先度を下げる)する未来は来ますか？ ■リポジトリの信頼性について ・リポジトリの信頼性を高めるために何をすべきですか？ ■「不完全なVRP」への対策について ・対策は必要だと考えますか？ ・判断するための要素として必要なものは何だと考えますか？ ・VRPブレーカーの仕組みに対してご意見を頂きたいです プログラムで扱う内容について 本プログラムでは、RPKIキャッシュサーバとリポジトリ間のネットワークの問題、リポジトリ自体に着目して「より安全にRPKIキャッシュサーバを運用し、ROVするにはどうするべきか」を考えます。 BGPルーター側の実装やオペレーション、RPKIキャッシュサーバーの個別のソフトウエアの実装、ROVで不正経路対策をすること自体の是非や有効性については議論しないものとします。

### バックボーンをスケールアウトで“運用する”段階へ ～ DDBR商用化までの歩みと、実運用に渡して見えた論点 ～
slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/janog58-pr-backbone-scaleout-kddi.pdf
KDDIはこれまで、Telecom Infra Project（TIP）における活動を通じて、バックボーンネットワーク向けホワイトボックスルータ（DDBR: Distributed Disaggregated Backbone Router）の仕様策定・技術検証を進めてきました。JANOG52では取り組みの背景とアーキテクチャを、JANOG56ではAI時代のトラフィック増大を見据えたスケールアウトネットワーク構想と商用導入計画を紹介してきました。 そして今回、DDBRを用いたバックボーンのスケールアウトネットワーク構築が完了し、商用運用フェーズへ移行しています。本発表では、これまでの取り組みを振り返ったうえで、机上の空論では終わらない、商用導入を経て見えた「実態」を余すことなく紹介します。具体的には、「オープン化/DDBRの導入により、何が本当に変わったのか？」「DDBRは、論理的に1台のルーターとして本当に動作するのか？」「設計から見えたスケール特性と運用のリアルな課題とは？」「マルチベンダー環境での責任分界点はどこか？」といった皆様が抱くであろう疑問に対し、綺麗事だけではない我々が実践から得た生々しい知見を、余すことなく共有します。最後に、DDBRを今後一般化していくために、運用・設計の観点でJANOGコミュニティとして議論すべき論点を提示し、皆さまと意見交換できればと考えています。 議論ポイント オープン化の普及には『仲間』づくりが不可欠です。 JANOGコミュニティの場で、各社の考えや方針、そして導入への課題を共有し、議論を深めたいと思います。 ①各社におけるネットワークオープン化の位置づけ・方針 オープン化は コスト削減・柔軟性・ベンダロックイン回避 のどこを主目的としているか ②オープン化に踏み出す際の最大の壁は何か 技術面（性能・品質）、運用面（切り分け、監視）、コスト面での課題・疑念

### 若手エンジニアは何を学ぶ？ 〜現在地とこれから〜
AIが当たり前のように学習ツールとして使われる今、若手エンジニアの「学び方/学ぶこと」は確実に変わりつつあります。 本セッションでは、入社〜5年目の若手エンジニアを対象としたアンケートをもとに、「今の若手が何を・どれくらいの時間をかけて・どんな手段で学んでいるか」をデータとして可視化します。そのうえで、若手からベテランのパネラー4名が、若手エンジニアのこれからについて語ります。 体系的な書籍、写経、ラボ構築 — ベテランが当たり前のように通ってきた学習の道筋は、AI時代でも有効なのでしょうか。あるいは、若手が自然と身につけている新しい学び方の中に、これからの新たな正解があるのでしょうか。 若手だけでなく、次の世代へ何かを継承するすべての方に来ていただきたいセッションです。 若手エンジニアのリアルな課題を出発点に、ぜひ会場で議論に参加してください。 議論ポイント – 若手エンジニアのリアルな不安と向き合う – 「エンジニアとして成長するには?」というキャリア不安をどう解消するか – 「AIに淘汰されるのでは?」という漠然とした恐怖にどう立ち向かうのか – AI時代における学習手法の再考 – 書籍による体系学習・写経・自前ラボ構築は、AI活用が前提の現代でもまだ必要か – インプットとアウトプットのバランスはどう変わったか – ベテランが若手から逆輸入すべきものは何か – 若手が自然に使いこなしている学び方・ツール・思考法で、ベテランが取り入れるべきものはある? – 組織にお願いしたい学習環境・OJT設計 – 調査結果から見えてくる「今の若手を育てる」支援とは何か？

### 本会議場内の飲食について
No overview published; title and speakers only.

### JANOGかるたイベント開催決定！！！
No overview published; title and speakers only.

### モバイル運用における生成AIの現場実践 〜基地局保守・コア保全から事故統制まで〜
slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/JANOG58_ソフトバンク_pr-genai-mobile-ops.pdf
通信インフラの運用現場では、障害発生時の迅速な状況把握と復旧対応、過去知見の活用、対応品質の均質化が継続的な課題となっています。一方で、生成AIを活用した取り組みは各所で進みつつあるものの、PoCにとどまる、または本番導入後に現場で定着しないといった課題も少なくありません。 本発表では、ソフトバンクのネットワーク運用領域において、生成AIを実運用に組み込み、現場で継続的に利用されている事例を紹介します。基地局保守領域では、生成AIを搭載したオンサイトシステムを全国の保全会社の作業員に展開し、アラームの解説や過去の対応履歴要約、被疑箇所推論といった機能を提供することで現場での自己完結的な対応をサポートしています。また、モバイルコアの保全領域では、AIが過去の障害チケットやログを自律的に読み解き、インシデント発生時の初動対応を支援することで、属人化の低減と対応時間の短縮を目指しています。 さらに、大規模障害時の音声会議に含まれる状況共有や判断内容をリアルタイムに構造化し、要約・影響整理・タスク抽出し、AIが事故統制をサポートする取り組みも進めています。これらの事例を通じて、生成AIを単なる検証に終わらせず、運用現場に定着させるための工夫と課題を共有します。 これらの取り組みは、特に新規メンバーからの評価が高く、NOCの人材育成という観点でも貢献できているものと考えています。 議論ポイント ・PoCから本番に進まない最大のボトルネックはどこにあると思いますか？（技術／コスト／組織） ・AIツールは“現場に使わせるべきもの”か、“使う人だけが使えばよいもの”か？利用率が上がらないAIツールは失敗とみなすべきか？ ・RAG、MCP、LLMでの深堀、もしくはその他の手段などどのようにデータを探索するか？ ・音声・動画データ活用は取り組んでいるか、コストに見合っていますか？ ・専門用語対応はRAGで十分か、それともFine-tuningが必要か？その更新を自動化できているか。 プログラムで扱う内容について 扱うこと – AIを活用した具体的な業務改善例 – AI利用を促進するための取り組み・評価 扱わないこと – 開発した環境・インフラについて

### ライトニングトーク
slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/07/Agentic-AIを活用したGitOpsベースの5GCデプロイメント_LT用-Koichiro-Kunitomo.pdf | slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/07/XDPerf_-High-Performance-Network-Traffic-Generator-Takeru-Hayasaka.pdf | slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/07/%E3%80%90%E7%99%BA%E8%A1%A8%E8%B3%87%E6%96%99%E3%80%91%E3%82%AD%E3%83%A3%E3%83%AA%E3%82%A2%E7%B6%B2%E3%81%AF%E5%88%86%E6%95%A3AI%E6%8E%A8%E8%AB%96%E5%9F%BA%E7%9B%A4%E3%81%AB%E3%81%AA%E3%82%8C%E3%82%8B%E3%81%AE%E3%81%8B%EF%BC%9F-Shuyu-Saito.pdf | slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/07/acmeLT-Kazunori-Fujiwara.pdf
開催日時 ：2026年07月16日 (木) 13:45 – 14:30 開催

### 遠くの国のモバイル回線をどう知るか
slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/JANOG58_遠くの国のモバイル回線をどう知るか_資料.pdf
海外のモバイル回線の様子を調べにいくことがありました。 通信環境がどんな感じかを調べるのにやった工夫やパターンを紹介したいと思います。 サーバがあればできること、スマートフォンのクライアントのやれることが限られた権限の中でできることを紹介します。 品質というには怖いですが、ユーザ環境がどんな感じかを知れるとアプリレベルの最適化の方向性を考えやすいと思っています。 議論ポイント 遠隔地・端末違い・など多様な実ユーザ環境を、どう測れるのか 不完全な測定結果を、意思決定に使える“傾向”としてどう扱うか

### JC2を考える
slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/janog58-jc2-shtsuchi-1.pdf
JANOGに参加してる皆さん JC2ってご存知ですか？現在ではJANOGも多くの人が集まり、色んな意見を頂く事が多くなってきたと思います。 JANOGミーティングの参加者も6000人を超える事もあり、 このままJANOG参加者が指数関数的に伸びていっていいのだろうか？ また健やかで自律したコミュニティでいられるか？という事も感じています。 JANOGの法律でもあるJC2を考えてみたいと思います。 https://www.janog.gr.jp/doc/janog-comment/jc2.txt プログラムで扱う内容について 会場との議論により下記内容が含まれる事が考えられます JANOG有料化 役員任期の適正化 不信任決議方法 会則変更の実現性

### ネットワークOSの運用ライフサイクルを考える – AIを活用したネットワークOS選定の省力化
slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/janog58-pr-nw-os-lifecycle-odagawa-yomogida.pdf
ネットワーク機器に搭載されるOSは年間を通じて継続的にリリースされており、安定した運用のためには定期的なバージョンアップが不可欠です。 各組織においても、NOS選定のポリシーや基準、導入・更新に関するライフサイクルが存在していると考えられます。 IIJでは、新しいNOSを導入する際に、実ネットワークで利用する機能が正常に動作するかを事前に検証することを必須としています。一方で、この検証には一定の時間と工数を要するため、ライフサイクルに沿った更新を進める上で、検証リソースの確保が課題となっています。 こうした背景のもと、IIJではAIを活用したNOS選定および検証の自動化に取り組み、一部で導入を進めています。 本発表では、IIJのユースケースを紹介するとともに、NOS選定における考慮ポイントや、選定・検証の省力化を目的として開発したAI活用型の自動検証ツールの仕組みと効果について共有します。また、理想的なOSライフサイクルのあり方や効率的な検証手法、AI活用の可能性について、参加者の皆様と議論することを目的としています。 議論ポイント NOSのライフサイクルについて、どのようなポリシーをお持ちですか？また、どのような基準でバージョンを選定していますか？ 機器検証やNOS検証は、どのようなフローで実施していますか？ NOS検証には、どの程度の工数・人数・期間をかけていますか？ AI（AI Agentを含む）の業務活用はどの程度進んでいますか？また、主にどの分野で活用されていますか？ 自動化ツールのメンテナンスやコードの保守は、どのような体制で行っていますか？

### 運用者自らどこまで自動化できるのか？ 〜ゼロタッチ運用の実践と継承課題〜
ネットワーク運用の自動化は、これまで特定業務の省力化を目的とした「部分最適」の取り組みとして発展してきました。 しかし、そのような自動化は一定の効率化を実現する一方で、運用全体としての省人化や持続的な価値創出にはつながりにくいという課題があります。 私たちはこの課題を、技術の「成熟」という観点で捉え直し、故障検知から復旧までをシームレスにつなぐ「全体最適」の運用へ進化させる必要があると考えました。 その中核となるのが、運用熟練者の暗黙知を形式知として体系化し、自動化へ組み込むことで実現するゼロタッチ運用です。 本取り組みでは、運用者自身が、運用知識を実装可能な形へ再設計し、自動化ロジックとして組み込むことで、単なる自動化にとどまらない「再現可能な運用」の確立を目指しました。 これは、技術を個人に依存させず、次代へ継承可能な形へ昇華させる取り組みを目指しております。 本講演では、2025年11月25日にプレスリリース※したゼロタッチ運用の開始をもとに、以下の重要ポイントをご紹介します。 1. 対処すべきアラームの判別（RCA）および伝送装置連携の自動化 2. サービス品質を維持したままの復旧措置と、安全なトラヒック迂回の自動化 3. ネットワーク組み込み自動化とゼロタッチ運用の連携 4. 自動化レベルを評価し、継続的に進化させるための取り組み 最後に、技術の成熟を前提とした他NW領域への横展開と、運用知識の継承をどのように実現していくかについて、今後の展望を交えてお話しします。 ※プレスリリース： https://www.softbank.jp/corp/news/press/sbkk/2025/20251125_02/ 議論ポイント 自動化はどこまで目指すべきか、生成AIの活用も含めて人が介在すべき領域はどこか 自動化は運用スキルの継承を促進するのか、それとも阻害するのか NOCをまたぐ自動化において、標準化と柔軟性をどのように両立するか 自動化の成熟度や価値をどのように評価・可視化すべきか 自動化を前提とした運用において、手順や設計変更への追従性をどのように担保するか

### Rack-Scale GPUサーバーのNW設計と運用までの苦悩
slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/j56-lt4.pdf | slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/janog58-pr-rack-scale-gpu-内田-泰広-張-朝程-1.pdf
ソフトバンクでは、自社で AI 計算基盤を運用しユーザに対して計算資源を提供しています。 今回初めての取り込みとして、大規模な Rack-Scale GPU サーバの設計・構築しました。 従来のAIデータセンタの設計・運用フローでは対応しきれない物理的・時間的制約が大きく、多くの学びを得ました。 本セッションでは、最新のAIデータセンタをどのように設計して構築していったか、運用までに出てきた課題をどのように解決してきたかについて発表します – 水冷特有の設備であるCDUやマニフォールド、ORv3ラックへの対応、Rack-Scale GPU サーバ特有の物理制約をネットワーク設計にどう反映したか – 構築期間短縮のためレイアウト最適化、運用フェーズで直面した課題への対応 今後、最新のAIデータセンタを構築する人が何を考え、何に取り組むべきかを明確化できるようなセッションを目指します。 議論ポイント – 構築期間を短縮するために物理・論理設計で取り組んでいることはありますか (配線・レイアウト・部材選定など) – ファシリティ周りの知識をどのように得ていますか(電源/冷却設備/ラックなど) – 最新のデータセンタ構築に向けて何を学び、何に取り組むべきか プログラムで扱う内容について どのような内容を共有するか 設計時の対応 ラックスケールGPUサーバをどのような考えで設計したのか マルチテナントをどのように実現したか 最終的に決まった構成に至るまでの背景 構築時・運用時の話 配線時に困った事・ブレイクアウトケーブルの課題 水冷ラック特有で困った事 リンクフラップ問題・トランシーバの切り分け手法

### WGをやってみよう
slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/janog58-pdwg-tsuchiya-00.pdf | slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/janog58-pd-wg-tomochika-00.pdf | slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/janog58-wg-softwire-wg-ohkubo-00.pdf
JANOGワーキンググループってご存知ですか？ https://www.janog.gr.jp/doc/janog-comment/jc4.txt https://www.janog.gr.jp/wg/ JANOGには短期集中型のワーキンググループがあります。 ワーキンググループで議論を行うメリットや体験談を通して、今アクションを起こしたい人の参考になればと思います。

### 景観保護のための空間光通信(FSO)活用事例 〜松山城周辺の観光を支える次世代インフラ〜
slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/07/J58_pr-fso_pre.pdf | slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/07/J58_pr-fso.pdf
本発表では、歴史的景観保護の観点から光ファイバーの敷設が困難な松山城周辺において、空間光通信(FSO)を用いた10Gbps級バックホールを構築した事例を報告します。 単なるリプレースに留まらず、Wi-Fi 7時代を見据えた10Gbps以上の帯域確保と、FSO特有の課題(霧、振動、光軸ズレ)をいかに現場レベルで解消したか、その選定プロセスと運用知見を共有します。また、FSOの有効性と注意点、他ワイヤレス技術との比較について、FSOの技術遷移とあわせて解説します。 実地での運用知見を元に、地域ISP/CATV事業者が直面する「ラストワンマイルの高速化」に対して、新たな選択肢に繋がるような議論交換を行います。 ※7/10追記 事前資料 をアップしました 議論ポイント 景観保護が必要な観光地・史跡でのインフラ構築における、様々なワイヤレス技術の活用について。

### 2026 WORLD BASEBALL CLASSIC™　～侍JAPANとJANOG侍の戦い～
slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/janog58-pr-wbc-yoshida.pdf | slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/janog58-pr-wbc-obinata.pdf | slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/janog58-pr-wbc-miyamoto-1.pdf
2026年3月に開催された、2026 WORLD BASEBALL CLASSIC™ では、NETFLIX独占配信の形で、インターネットオンリー環境で野球が中継された。本大会に備えるため、NETFLIX及び各通信事業者の間で過去に類を見ないレベルでの回線設備の増強やバックボーン増強を行い、当日も六本木にCONECT JAPAN NOCを設け、事業者間で協力をすることで大きなトラブルなく国内最大のネット配信が実現した。しかしその裏には様々な苦労があり、初戦18時の戦い、アクセス網の戦い、祈り、想定外の事象など。また同時にNETFLIX最新配信技術によりコンテンツ配信においても様々な工夫があり、興味深いトラフィック特性なども見られた。今回の発表では、約半年にわたるJANOG侍の戦いについて共有すると共に、超大規模なネット配信イベントに今後通信事業者はどう備えていけば良いか、JANOGの皆さんと議論したい。 議論ポイント ・不測の事態に備えるため、コンテンツ配信事業者と事業者連携はどう連携していくと良いか ・現地NOCの重要性、リアルな情報共有について ・QoE観点でどういう結果だったか、人が視聴するレベルでのトラフィック量と質 ・様々な今後の巨大ネットイベントに今後どう備えるか、キャパシティー設計、維持管理の悩み ・単一CDNとマルチCDNの違い ・イベントの重なりを避けるには？など

### どうする?どうなる?　これからのログ保存
slides: https://www.soumu.go.jp/main_content/001030755.pdf | slides: https://www.soumu.go.jp/main_content/001017843.pdf | slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/07/pr-log-storage_morikawa.pdf
通信ログ保存の在り方に関するワーキンググループにおいて 通信ログ保存に関して従来のガイドラインを大幅に変更することが検討されています。 従来のログ保存のガイドラインにおいては、業務上必要最小限の保存を認めるといったものでしたが 通信ログ保存WGでは、誹謗中傷や違法・有害情報への対応、警察捜査への協力といったものについても 対応が求められCP（SNS・掲示板等）AP（アクセスプロバイダ）の双方において、一定期間の通信ログ保存が 業務の一環として社会的に期待されるとされています。 通信ログ保存のあり方が大きく変更される事による課題や問題点などを共有できればと思います。 https://www.soumu.go.jp/main_content/001030755.pdf https://www.soumu.go.jp/main_content/001017843.pdf https://www.soumu.go.jp/main_sosiki/kenkyu/ICT_services/02kiban18_02000413.html 議論ポイント 今回のガイドラインの改正において、ログ保存の立ち位置が大きくかわる事になります。 従来の電気通信事業法および同ガイドライン解説は、 通信履歴は「通信の秘密」に該当し得る 記録・保存は原則抑制課金やユーザーサポート、設備運用など業務必要性に限って「正当業務行為」として必要最小限の保存が認められてきた。 所謂、保存の上限が決められていた。 しかしログ保存WGでは、誹謗中傷や違法・有害情報、警察への捜査協力への対応という、必ずしも従来想定されていなかった目的についても、 一定期間の通信ログ保存が業務の一環として社会的に期待されるとして事業者側にログ保存が求められている。 これは法的に保存義務を課すものではないものの、3～6か月のログ保存を事業者側に強く求めています。 これらの点において、今後事業者としてどのように対応していくのか議論できればと思います。

### NOC全体に生成AIを届ける　〜閉域商用網で使えるセキュアなAI共通基盤づくり〜
slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/janog58-pr-secure-genai.pdf
私たちソフトバンクでは、商用ネットワークを運用するNOCにおいて、生成AIを活用した運用高度化に取り組んでいます。近年、ネットワーク運用におけるAI活用や自律化に関する議論は活発になっていますが、商用ネットワークのように高いセキュリティ要件や閉域性を持つ環境では、LLMをそのまま利用することが難しく、技術面・運用面の双方に多くの課題があります。 本発表では、NOC内でAI活用を推進するNOC内の専任チームが、約1年以上にわたり自分たちで構築してきた、商用ネットワーク運用向けの生成AI活用基盤について紹介します。 具体的には、閉域環境から安全にLLMを利用するための共通接続基盤、センシティブ情報を扱う現場でも利用しやすいOpenWebUIを用いたAI-Chat環境、NOCメンバー自身が業務自動化を試行できるローコード基盤（Dify）、さらにコード生成・実行を安全に扱うためのAI Coding Agentなどの取り組みを取り上げます。 これらは単なるツール導入ではなく、NOCの業務プロセスや利用者への浸透を含めた、AI中心の運用へ移行するための土台作りでもあります。商用ネットワーク運用という制約の多い環境で、どのように安全性と利便性を両立し、現場に使われるAI基盤を育ててきたのか、その知見と苦労を共有します。 議論ポイント ・NOCメンバーや保全メンバーが、オペレーション環境で使える「AI活用環境」はなにがありますか？ ・運用メンバーはどのくらいがAIが浸透・活用しているか。また、DifyやOpenWebUIのような『自由度の高い環境』を渡すのが正解か、それとも特定業務に絞った『専用ツール』として提供すべきか？ ・閉域網制約下で、どこまでOSSに頼るべきか？ メンテナンスコストをどう見積もるか？ ・AI基盤は誰が作るべきか。情シス？NOC？それともSaaS？ プログラムで扱う内容について 扱うこと – AIを社内で活用するためのプラットフォーム構築 扱わないこと – AIを活用した具体的な業務改善例

### 日本のBGP運用
slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/日本のBGP運用（松崎）.pdf
日本のBGP運用は比較的精緻で安定していると考えられています。これは黎明期からIXPやJANOGなどコミュニティがそれを支えてきたのと、密なピアリングや精緻なIRR登録などが貢献してきたと考えています。一方で、変化に対しては機敏ではなく、徐々に過去の運用が習慣化して、更新されないままになってしまうことも懸念されます。また、運用者の世代交代なども進んで来ており、これまでのような事業者間での柔軟な意見交換が難しくなっていくことも懸念しています。このセッションでは、そうしたこれまでの状況と問題意識を会場と共有した上で、今後のBGP運用について会場と議論したいと考えています。 議論ポイント 日本のBGP運用は安全なのか – 足りてないところ – 新たなリスク RPKI ROA/ROVはこのまま進められるか – 足りてない情報 – 残る課題 ASはどう生き延びていけるのか – コスト問題 – 小さなAS

### マルチベンダーバックボーンで実現するDDoS対策 ～RFC Internet-DraftのBGP Flowspec Redirect-to-IP導入への挑戦～
slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/janog58-pr-multivendor-ddos-biglobe.pdf
BIGLOBEのバックボーンネットワークは、マルチベンダー(3社7モデル)にて構成しています。 このバックボーンネットワークにDDoSミティゲーション機能の導入のため、様々な方式を検討した結果、BGP Flowspec Redirect-to-IPを導入しました。 Redirect-to-IPは、BGP Flowspecを用いて送信元IP/宛先IP/ポート番号等にマッチしたパケットを、指定したネクストホップに転送する技術で、まだRFCのInternet-Draftの段階にあり、ルーターベンダーごとに参照しているドラフトのバージョンが異なり、実装に互換性がありませんでした。 https://datatracker.ietf.org/doc/draft-ietf-idr-flowspec-redirect-ip/ BIGLOBEでは、この非互換性の解決のため、独自の変換装置を開発・商用導入しました。この装置は、フローコレクタからのRedirect-to-IP経路を、各ルーターの実装に合わせて変換し、マルチベンダー環境全体でDDoSミティゲーションを正しく動作させるものとなっています。 このプログラムでは、このBIGLOBEの技術的な挑戦と工夫について詳しく紹介し、ご参加の皆様と、Flowspecの活用事例や、マルチベンダー環境のメリット・デメリット、そしてRFCドラフトを商用環境に導入する際の考え方などについて、議論を行いたいと考えています。 議論ポイント ・DDoSミティゲーション(スクラビングへの引き込み)には様々な方式がありますが、どのような方式で導入されていますか ・BGP Flowspecは10年ほど前によく話題になっていましたが、実際にどのような目的で商用利用されていますか。商用利用にあたって課題になった事はありますか ・マルチベンダーを採用する事によって、品質向上やコスト改善のメリットはありますが、機種数の増大で運用コストの増加に繋がっていると感じていますが、どう改善されていますか ・Internet-Draft段階のRFCの商用導入においては、Standardになるまでに非互換の変更がされる事がありますが、どのように乗り越えていますか

### 【和室で開催】JANOG57で話題となった、ネットワークの基礎を学べるボードゲームで一緒に遊びませんか？
slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/07/J58_pd-network-board-game.pdf | video: https://www.youtube.com/watch?v=n20srMkJuPA
普段はネットワークの運用業務をしていますが、本業の合間に、ネットワークの基礎や運用の考え方を楽しく学べるネットワーク学習ボードゲームを作成しました。 今回のJANOG58のテーマである「技術の成熟と次代への継承」にもあるように、成熟してきたネットワーク技術や運用の知見を、次の世代へどのように伝えていくかは大切なテーマだと考えています。 このボードゲームでは、ネットワークの構築、トラブル対応、冗長化、ネットワーク分割といった考え方を、実際に手を動かしながら体験できます。子どもや初学者にもネットワークに興味を持ってもらうきっかけを作り、将来的なネットワークエンジニア人口を増やしていきたいと考えています。 JANOG57の野良BoFでも本ボードゲームの体験会を実施し、参加者の皆さまに実際に遊んでいただきました。今回は、JANOGの通常プログラムのような発表・議論中心の形式とは少し異なり、参加者の皆さまに実際にボードゲームを遊んでいただく体験会に近い内容です。プレイ可能人数は、最大24名（4名×6卓）を予定しています。 実際に遊んでいただき、「面白かった点」「分かりにくかった点」「もっとこうした方がよい点」など、率直なご意見をいただきたいです。気軽に遊びに来てください！ また、ボードゲームの感想だけでなく、次世代のNWエンジニアを育成するための施策や、子ども・初学者にネットワークへ興味を持ってもらうための取り組みについても、皆さまと話し合いたいです。 議論したいポイント ・ボードゲームを実際に遊んでみた感想や改善点 ・子どもや初学者にネットワークへ興味を持ってもらうための工夫 ・次世代のNWエンジニア育成に向けたアイデア

### 人のための自動化がAIエージェント運用への道を拓く ― IOWN APN × VXLAN/EVPNをまたぐマルチレイヤ抽象化の実践
slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/janog58-pr-automation-yoshi-suzuki-01.pdf
クラウド利用や生成AIの普及により、DC間トラフィックは増大の一途をたどっています。私たちは、複数拠点のDCをEVPN/VXLANとIOWN APNで結ぶ分散DCアーキテクチャを、技術開発・サービス開発を通じて社会実装させていきたいと考えています。 しかし、いざこの基盤を運用するとなると課題に直面することとなります。 私たちは、IOWN APNをDC間バックボーンに用いた3拠点の分散DC基盤を構築し、多数の実証実験を支えてきました。しかし、この基盤を日常的に運用管理しているのは少数のメンバーです。 少数での運用にも関わらず、その運用には広く専門的なスキルが求められます。Cisco NexusによるVXLAN/EVPNのL2/L3オーバーレイ、Fujitsu・NEC・Ciena といったAPN（光伝送装置）によるL1パスの構成、そしてそれらをまたぐマルチベンダー・マルチレイヤの設計・障害対応など。 現場では、 ・光（波長・回線）とオーバーレイ（VXLAN/EVPN）を別システム・別手順で構築・変更 ・案件やユーザー単位の変更や切り戻しが難しく、運用が属人化する ・障害時は物理・論理の対応関係を手動管理し、リアルタイムな状態把握にも手間がかかる といった課題に日々向き合っていました。 本発表では、この「少人数×マルチレイヤ」という制約の中で取り組んできた自動化・可視化の実装と知見を共有します。具体的には、 ・ネットワークオーケストレータを核に、光波長パスとVXLANを案件やユーザー単位で一括構築・変更できるシンプルなAPI ・マルチベンダー・マルチレイヤ環境でのトランザクション整合性の確保 ・物理〜論理レイヤを跨いだ対応関係をDB化するとともに、各デバイスからライブステータスを定期取得し、少人数でもリアルタイムに全体を把握できる可視化 を紹介します。 さらに、これらのシンプルなAPI・トランザクションの一貫性・構成情報とライブステータスの取得基盤は、AIエージェントがネットワークを理解し操作するためのインターフェースとしても機能します。本発表では、AIエージェントが自然言語の指示をもとにマルチレイヤ環境の情報収集・設定変更・状態確認を自律的に行うデモを実施し、少人数運用の次の一手としてのAI活用の可能性をお見せします。 議論ポイント 運用の属人化、どう向き合っていますか？ • ベテラン頼みになっていませんか？ • スキルトランスファーや自動化、どこまで進められていますか？ AIエージェント、もう触っていますか？ •取り入れていますか？まだ様子見ですか？ • 触ってみて「これは使える」「これは無理」と感じたのはどんなところですか？ AIのハルシネーション、怖くないですか？ • 商用環境で使うとしたら、何があれば安心できますか？ • 「これがないと無理」という前提条件は何ですか？ AIエージェントを動かす土台、何を整備しましたか？ • API、トランザクション管理、ライブステータス取得、ドキュメント…… • まず何から手をつけるべきだと思いますか？ AIと人、どう役割分担しますか？ • AIに任せたい領域・任せたくない領域は？ • 運用者の役割はどう変わっていくと思いますか？

### アドレスポリシーの成熟と継承～ポリシーの意義・将来を考えよう～
slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/アドレスポリシーの成熟と継承～ポリシーの意義・将来を考えよう～花井直樹_中川香基.pdf
アドレスポリシーは、普段のネットワーク運用の中で意識する機会が多いテーマではありません。しかし、IPアドレスの割り振り条件や利用のあり方に関わるものであり、通信事業者やネットワーク運用者にとって決して無関係なものではありません。実際に、ポリシーの変更は、資源の受け方や設備設計、将来の事業運営にも影響し得ます。 一方で、アドレスポリシーの議論は仕組みや参加方法も分からないと言う方も少なくないと思います。また近年、JANOGの場でも幾度か取り上げられてきたトピックではあるものの、関心があっても議論に入りづらい状況があるのではないでしょうか。だからこそ本プログラムでは、単に制度を紹介するだけではなく、アドレスポリシーを運用者コミュニティの中で改めて自分たちの課題として捉え直し、国内コミュニティが今後どのようにこの議論と向き合うべきかを参加者とともに考える場にしたいと思います。 プログラム前半では、アドレスポリシーとは何か、またその策定プロセスであるPDPについて基本から整理します。そのうえで、過去の重要な議論や現在提案されている論点を紹介し、後半では参加者とのディスカッションを中心に進めます。たとえば、IPアドレスのリースをどう考えるべきかなど、今後どのような論点が出てきそうか、そして新しい参加者をどう議論の場に呼び込んでいくべきか。そうした問いを出発点として、アドレスポリシーを「知っている人だけのもの」にしないために、JANOGの場で何ができるのかを議論したいと考えています。 議論ポイント ・現行のアドレスポリシーに感じる課題はあるか ・運用上困っていること、変えたいところはあるか ・ポリシー提案議論に参加するにはどうしたらよいか ・ポリシー議論の場を盛り上げ、コミュニティの関心を呼ぶには何が必要か ・現在アドレスポリシー議論に足りていないものは何か、参加の障壁・要因は何か ・JANOGでの議論をJPOPM/APNIC OPMでの議論へコミットさせるには

### NWトポロジー可視化から時系列化へ: BGP-LS+BMP+αによるトポロジー把握の時間軸拡張
slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/07/【事前公開用】JANOG58_pr-topology-timeseries.pdf | slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/07/janog58-topology-timeseries-uchimi-main.pdf
従来、ネットワークの異常検知やトラフィック監視には、SNMP、NetFlow、sFlow、各種Telemetryといった技術が広く用いられてきました。これらはインターフェーストラフィック量やCPU・メモリなどの装置リソース監視において非常に有効であり、現在も重要な役割を担っています。 一方で、大規模かつ複雑な実運用ネットワークにおいて、動的に変化するルーティングプロトコルの内部状態や、ネットワーク全体の論理トポロジー、経路変化の前後関係をリアルタイムに把握することは、従来の監視手法だけでは難しいと考えています。JANOG54で報告したTelemetry活用も個別装置の監視には有効でしたが、ネットワーク全体のトポロジー変動や経路状態の推移を継続的に捉えるには別のアプローチが必要です。 この課題に対するアプローチとして、BGPの監視・収集を目的としたBMPや、IGPトポロジー情報をBGP経由で外部へ取り出すBGP-LSが実装されています。BGP-LSは主に論理トポロジーやリンク状態の把握に、BMPはBGP経路状態やその変化の観測に有効です。これらを組み合わせて時系列で保存することで、「ある時点でネットワークがどのようなトポロジーだったか」を継続的に追跡できる可能性があります。 大規模・複雑な実運用網において、トポロジーの鮮度をどう担保し運用判断に使える情報へ落とし込むかは、多くの事業者に共通する論点であると考えています。そのため実運用上どのような情報が必要か、またそれに求められる要件についても、JANOGの場で議論したいと考えています。 本発表では、BGP-LSおよびBMPを用いてネットワークトポロジーをリアルタイムに収集し、時系列データとして保持する仕組みと、そこから任意時刻の状態再構成を試みた結果を紹介します。あわせて、障害時の解析や事後検証、構成変更前後の状態比較といったユースケースの案を示しつつ、観測結果を検証環境やNDTへどう接続するか、L3観測だけでどこまで十分か、静的な構成情報と動的な観測情報をどう組み合わせるべきかについて議論したいと考えています。 議論ポイント 議論ポイント1 BGP-LS/BMPにより、トポロジーの時系列観測は可能になりつつある。 一方で、その観測結果を検証環境やNDTへ接続し、再現・予測に活用するには何が足りないのか。 観測データから検証・シミュレーションへ橋渡しするために必要な中間モデルや補完情報について議論したい。 議論ポイント2 今回の取り組みで把握できるのは主にL3制御プレーンの状態である。 実運用において、L3トポロジーの時系列観測だけでどこまで十分なのか。 また、逆にL1/L2や設備台帳など他レイヤ・他系統の情報が必要になるのはどのようなユースケースかを議論したい。 議論ポイント3 静的な構成情報とBGP-LS/BMPで得られる動的な観測情報を、どのように組み合わせれば運用判断に使える情報になるのか。 データの保持期間やサンプリング粒度、フラッピング時の扱い、また観測されたStateと構成管理上のIntentが一致しない場合にどちらを正として扱うべきかを議論したい。

### AI showcase LT〜見せます私のAI活用方法〜
slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/06/コードの99をAIが書くネットワーク運用部署の次の課題-Tomoya-Watanabe.pdf | slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/06/260626_Janog58LT_AgenticLoopなネットワーク検証-Nobuaki-Kadowaki.pdf | slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/06/Devinに検証環境を丸ごと渡して、-設計判断の材料集めを任せてみた-2.pdf | slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/06/JANOG58_AI-showcaseLT_LLMで3GPP標準化提案文書を読み切る_NTT-DOCOMO.pdf
本LTについて 採用方法 採用プログラム一覧

### AIが工事を担う時代に技術者は育つのか　～現地完結型が突きつけるスキル維持の課題～
slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/JANOG58_現地完結型_資料.pdf.pdf
NW構築・保守の現場で発生する運用中の装置に対する「現地と遠隔の相互確認（2Way）」は、安全品質を担保するために必須の工程と考えられています。 しかし、広域を1つの遠隔組織で支える体制では、工事件数が増える局面（例：大規模移行で大量工程が発生する局面）で遠隔側の作業枠がボトルネックとなり実施可能な工事数が制限されるというジレンマが発生していました。 そこで私たちは、固定概念だった「現地と遠隔の2way」を見直し、チャットボットを介して現地が手順・確認点の指示を受けつつ、遠隔側の作業（Config投入・確認など）は自動化PFで実行する「現地完結型工事」を導入しました。 現地完結型工事が一般的になるにつれて、作成すべき自動化シナリオの数は急増し、工事担当組織ごとのシナリオ品質のばらつきやシナリオ作成が可能な有スキル者の育成・確保 が新たな課題として浮かび上がりました。 これらの課題に対し、「自動化PF開発標準」やCopilot エージェントによるシナリオ作成自動化の仕組みを整備し品質向上と稼働削減を実現しています。 一方で、現地完結型工事の進展により遠隔工事を通じて経験や作業の勘所を積む従来のキャリアパスが断たれるという別の課題も生まれています。 本発表では、現地完結型工事を支える自動化PF運用と、開発プロセス標準化を前提にしたAIエージェントによるシナリオ作成自動化の構想を紹介します。 そのうえで、「確実性が強く求められる工事シナリオ作成という領域にどのようにAIを取り入れていくべきか」「AI全盛時代に技術者をどう育て、スキルをどう維持するか」について、参加者と議論したいと考えています。 議論ポイント ・「現地完結型」のような仕組みはメリデメあると思いますが各社やってますか？ ・自動化プラットフォームは内製・独自部分が多いですか？ ・「自動化PF開発標準」のような組織横断の品質維持の取り組みはやってますか？ ・人員減耗、AI全盛のなか、現場のキャリアパスはどのように変わっていくべきでしょうか？ ⇒MEでは有スキル者の育成・維持は必須と考えてます。

### 朝から晩まで MCP　—　AI エージェントと私
日本大学は 10 万ユーザーを抱える総合大学。多くのキャンパスに分散したインフラを少人数で運用管理するため，Juniper PyEZ・Zabbix API・Google API など各種 API を叩く Python/Shell の自作スクリプト群を積み上げてきた。そこに AI エージェントを組み合わせ始め，業務ツールを MCP（Model Context Protocol）として作り直し，Claude Code から利用するケースが増えてきた。気付けば朝のパトロールから報告書作成まで，業務はほぼ Claude 越しになった。 本セッションでは大学情シスの一日を時系列で追いながら，MCP 活用の実際を共有する。朝は Zabbix MCP・KeyCloak MCP と xFlow・Shadowserver でアラートと認証ログを一括チェックし，junos-mcp・aruba-central-mcp・eos-mcp でキャンパスネットワーク機器の一括ヘルスチェックも行う。日大公式 Web のパトロールも AI エージェントで自動化した。昼は junos-ops（PyEZ/NETCONF）で設定の差分レビューを行い，dry-run 経由で投入する。夕方は GWS MCP でのメール送信，ドキュメントを Markdown で生成して Box へ自動同期する運用も紹介する。 併せて MCP 導入で顕在化した課題 — stdio の限界，Streamable HTTP OAuth2 への移行，MCP サーバの開発・運用管理・セキュリティ保全，LLM 暴走防止の設計パターン — を共有し，会場と議論したい。 議論ポイント – ネットワーク運用業務における MCP の「効く場面」「効かない場面」の現場感を共有したい – 自作 MCP サーバを OSS として公開する判断基準（組織固有情報の切り分け，コントリビュート受け入れ態勢，MCP 品質向上計画） – stdio / Streamable HTTP OAuth2 など MCP サーバの認証・配布方式，皆さんは何を選んでいるか – AI エージェントが投入した設定変更の監査・ログ保全，トレーサビリティの確保方法 – ぼっち情シス／少人数運用で実際に効いている MCP ツールと，今欲しい MCP サーバ（会場アンケート的に） プログラムで扱う内容について TBA 使ってるMCPの概略 ツール 概要 使用例 junos-mcp Juniper 機器を NETCONF で操作する MCP サーバ（自作 OSS） 朝のルーティング・IF状態確認から設定変更の dry-run・rollback まで eos-mcp Arista EOS の eAPI を MCP 化（自作 OSS，16 ツール） daily_briefで温度/電源/errdisabled/MLAG を一括確認 aruba-central-mcp Aruba Central 無線 LAN クラウド管理 API の MCP 化（自作 OSS） AP/クライアント状態の参照と集計，トラシューに活躍 keycloak-mcp KeyCloak Admin REST API の MCP サーバ（自作 OSS，21 ツール） ユーザ検索・認証ループ自動検出・ログイン統計 GWS MCP Google Workspace API CLI を MCP 化（自作 FORK） メール文案壁打ち →送信，日常事務を MCP に寄せた mcp-stdio stdio と Claude Code の間の中継レイヤー（自作） stdio MCP の接続安定化・認証補完等

### ユーザ影響規模に縛られない次世代夜間作業の作法　～止められないNWを、止めずに変える～
slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/janog58-pr-nextgen-night-work-nttdocomo.pdf
本資料は、総務省重大故障ルールの厳格化や人材不足を背景に、NWを止めずに変える「次世代夜間作業」の実現方法を示している。SaaSを用いた計画作業の自動化・無人化や、自律AIによる障害復旧手順レコメンドの実証を通じ、影響が限定的な領域から夜間作業の無人化を進めた。今後、複数の自律AIとオーケストレータAIを組み合わせ、大規模装置を含む夜間作業の自動化拡大を目指す、あるいは他の基幹システムに展開していくうえで直面する課題感や無人化の必要性について議論したい。 議論ポイント 夜間作業の作業者立ち合いは必須とすべきか否か 運用業務領域でAIが活躍する/AIに任せられる業務とはなにか。 プログラムで扱う内容について プログラムで扱う内容（共有する内容） ・抱えている課題や取り組みに至った背景や経緯など ・システムアーキテクチャ ・運用で得られた知見 ・今後の改善ポイント など プログラムで扱わない内容 ・利用サービス・製品の詳細情報 など

### コミュニティ紹介LT -JANOGから広げる繋がり-
slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/08/pd-community-lt_moriishi.pdf | slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/07/pd-community-lt_ohgai.pdf | slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/07/pd-community-lt_momoi.pdf | slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/07/pd-community-lt_uchiyama.pdf
この分野興味あるんだけど、周りにやっている人がいないんだよな… 名前は聞いたことあったんだけど、実際どんなコミュニティなのか知らないんだよな… 同志と出会いたいそこのJANOGerのあなた、ぜひコミュニティ紹介LTに参加してみませんか？ このLTでは、JANOGでも時々耳にするコミュニティをコアメンバーの皆さんに紹介いただきながら、 「こんな取り組みがあったんだ！」「こういうコミュニティがあればいいな」といった発見・議論に繋げていきます。 このJANOGを起点に新たな繋がりが、仲間が、継承が生まれる場になれば幸いです。 コミュニティ紹介用のGoogleスライドについて 下記4つのコミュニティに加えて、JANOGerの皆さんが普段所属しているコミュニティを紹介・共有するためのGoogleスライドを用意しました。(JANOG58閉会に伴い、現在は閲覧のみ可能です) テンプレートをコピーして、①コミュニティ名・②記入者・③概要・④こんな人におすすめ・⑤コミュニティのURL(WEBページやSlackなど)・⑥ひとことを記載してください。 本スライドはLTの対象外ですが、プログラム内で眺める時間を設ける予定です。 コミュニティ紹介LT -JANOGから広げる繋がり- コミュニティ紹介LT -JANOGから広げる繋がり- コミュニティ紹介スライド docs.google.com 発表者とコミュニティ JADOG(Japan Datacenter Operators’ Group) 発表者 森石 浩徳(株式会社STNet) 資料 登壇資料_森石 浩徳 NeGI NOC (Next Generation Ikusei NOC) 発表者 大谷 亘(一般社団法人日本ネットワークインフォメーションセンター) 資料 登壇資料_大谷 亘 一般社団法人日本シーサート協議会(Nippon CSIRT Association) 発表者 ももいやすなり(株式会社インターネットイニシアティブ) 資料 登壇資料_ももいやすなり JAIPA AIワーキンググループ 発表者 内山 貴允(株式会社NTTドコモビジネス) 資料 登壇資料_内山 貴允

### 『坂の上の雲』へ続く道は、どこにあるのか ― ネットワークに関わる人の最初の一歩と、その先へのつながりを考える ―
slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/07/janog58-pr-sakanouenokumo-nezu.pdf | slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/07/janog58-pr-sakanouenokumo-maemura.pdf | slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/07/janog58-pr-sakanouenokumo-kawamura.pdf | slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/07/janog58-pr-sakanouenokumo-kudo.pdf
ネットワーク技術や運用の知見を次代へ継承していくうえで、若手を含むネットワークに関わる人たちが、どこから最初の一歩を踏み出し、どのようにその先のより広い場へつながっていくのかは重要なテーマです。一方で、日々の運用や地域・コミュニティでの活動の延長線上には、IETFのような技術標準化の場、IGFや日本IGFのような議論の場、育成プログラム、各種フェローシップなど複数の道があるにもかかわらず、その全体像やつながり方は必ずしも見えやすく共有されていません。本プログラムでは、それぞれ異なる道に関わってきた登壇者が、「最初の一歩はどこにあるのか」「何が壁になるのか」「誰が何を支えられるのか」「経験をどう次につなげるのか」を持ち寄り、参加者とともに議論します。特別な人だけの話としてではなく、日々の実務や地域、コミュニティの延長線上にあるものとして捉え、次の世代につながる道筋を考える場にしたいと考えています。 議論ポイント ・ネットワークに関わる人にとって、最初の一歩になり得る場には何があるか ・IETF、IGF、日本IGF、各種育成プログラム、フェローシップ等の道は、どのようにつながり得るか ・費用、言語、テーマ設定、伴走者の有無など、実際に何が壁になるのか ・本人だけでなく、送り出す側・受け止める側・地域コミュニティに何ができるか ・単発参加で終わらせず、国内コミュニティや所属組織に経験をどう還元できるか ・その先に、どのようなコミュニティやネットワークのあり方をめざすのか プログラムで扱う内容について 【共有したいこと】 ・現時点において、定量調査で把握できているJANOGerをはじめとするエンジニアが感じている不足感 ・若手が最初の一歩として触れうる、複数の場の存在 ・若手本人から見た壁 ・送り出す側、支える側から見た課題 ・単発参加で終わらせず、次につなぐために必要なこととは

### NOCいよかんトーク～24/365のリアル語って、未来への「いい予感」創るぞなもし～
JANOG55/56/57にて継続して実施してきた、各社のNOCが登壇し運用のリアルや課題感を持ち寄って議論するプログラムの続編です。（参考資料参照） これまで、障害対応、ツール活用、イベント時対応、若手視点でのNOCのあり方など、各回ごとに異なる切り口で各社の知見や運用の裏側を共有してきました。NOCが持続的に機能していくためには、多様な立場の人が継続して活躍できることが重要です。 しかしながら、メンバーにもそれぞれ出産・育児・介護というようなライフステージの変化があり、24/365の現場で働き続ける上での難しさも抱えています。さらには、自動化が進む運用の中で「機器を直接触って障害復旧させる経験」が減りつつあり、若手がどのように故障対応力を養い、実戦的な判断力を身につけるかという点も大きな課題となっています。 JANOG58のテーマは「技術の成熟と次代への継承」です。そこで、若手・エルダー・女性など、多様な立場や視点を持つ登壇者を集め、NOCで培われてきたノウハウ・コミュニケーション・働き方をどのように次代へつなぐべきなのか、その本質を浮き彫りにしていきます。 さまざまな背景を持つ人がどのようにNOCで活躍し続けられるのか、また、そのためにどのような支え方や向き合い方が必要なのかを、価値観や技術が著しく変化する今だからこそ、会場の皆さまとともに深掘りしていきたいと考えています。 本セッションでは、NOCを取り巻く重要な課題についてパネルディスカッション形式で議論し、登壇者とご来場の皆さまの間での有益な意見交換を目指します。 議論ポイント 1. 業務効率化 vs 育成 2. NOCコミュニケーション特有の課題 3. なりたい仕事ランキング1位になるには

### AIインフラ時代のデータセンター内光配線の実践知 ～高密度実装の課題と解決策～
slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/janog58-pr-dc-optical-cabling-Takashi-Inoue-3.pdf
AIインフラの発達により高速・高密度化が進むデータセンターでは、光配線はもはや単なる施工の話ではなく、ネットワーク設計、運用性、保守性、将来拡張性を左右する重要な設計要素になっています。 一方で、Opticsの進化、ラック仕様の多様化、水冷化の進展に対し、現場の配線設計や運用ノウハウの共有はまだ十分とは言い難い状況です。 本セッションでは、実際の大規模計算基盤の構築事例をもとに、最新の高密度光配線の現場を写真付きで紹介し、JANOG56で取り上げた内容からこの1年で何が変わり、何がむしろ難しくなったのかを整理します。加えて、現場で直面した課題と解決策を、施工・運用の両面から具体的に共有します。さらに光配線の専門コンサルタントである菊地様とともに、配線しやすいラック仕様、ラックレイアウトの工夫、MPO多心化、WDM opticsによる芯数削減、施工作業において重要なことなどを議論し、今後の設備設計と人材育成のあり方も問いかけたいと考えています。 光配線を“後工程”として扱う時代は終わりつつあり、その前提を会場の皆さまと改めて見直したいと思います。 議論ポイント • 光配線に関して何を大事にしているのか、どんな人が何を担当しているか • 配線しやすいラックの仕様、配線を考えたラックレイアウトや工夫ポイント • 設計側と施工作業者とのコミュニケーションはどのように行っているか • WDM Opticsの採用による芯数削減の効果と現実性 • 最新技術動向（シャッフルアーキテクチャ、MPO32の可能性など） • 光配線、Opticsの選定・運用ができる技術者の育成はどうしているのか プログラムで扱う内容について TBA

### インタラクティブLT
slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/脱・人間計算機！AIで光NWグランドデザインの手作業地獄から抜け出す_増田陽.pdf | slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/証明書が47日に短縮されます_海老澤直輝.pdf | slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/DGX-Sparkで5G-UPFを動かしてみた_平井志久.pdf | slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/ネットワークエンジニアが読むべきPQC移行に関するガイドラインの紹介_須賀祐治.pdf
毎回の参加者アンケートで、LTでも質疑があると良いとの意見が出ています。 今回新しい試みで本インタラクティブLTではプレゼンテーションの時間は決めず 合計75分を応募人数(最大採用人数7名)で割る短いプログラムを実施したいと思います。 割り当てられた時間は登壇者が自由に発表時間と質疑時間を決める事が出来ますが1-2個の質疑を受けるために 最低3分のQAの時間を設けたいと思います。 採用プログラム一覧 発表順 タイトル 発表者所属 発表者氏名 1 脱・人間計算機！AIで光NWグランドデザインの“手作業地獄”から抜け出す～全パス網羅評価でエンジニアは「計算」から「判断」へ～ 双日テックイノベーション株式会社 増田 陽 2 証明書が47日に短縮されます アカマイ・テクノロジーズ合同会社 海老澤 直輝 3 DGX Sparkで5G UPFを動かしてみた NTTドコモ 平井 志久 4 ネットワークエンジニアが読むべきPQC移行に関するガイドラインの紹介 株式会社インターネットイニシアティブ 須賀 祐治 応募資料 脱・人間計算機！AIで光NWグランドデザインの“手作業地獄”から抜け出す_増田陽 証明書が47日に短縮されます_海老澤直輝 DGX Sparkで5G UPFを動かしてみた_平井志久 ネットワークエンジニアが読むべきPQC移行に関するガイドラインの紹介_須賀祐治 LTプログラム募集について 募集期間 募集開始：2026年 7月 13日 (月) 10:00 [JST] 募集終了：2026年 7月 16日 (木) 10:00 [JST] 採用数：最大7LT 採用通知：2026年 7月17日 (金)10：00までに、応募者宛に電子メールにてお知らせします。 期間中は先着順に選考を行います。採用上限に達した場合、募集は早期終了します。 応募方法 募集を終了しました。たくさんのご応募ありがとうございました。 留意事項 JApanNetwork Operators’ Group Policy に基づき、営業活動が目的と思われる発表はできません。 JANOG行動規範 に基づき、あらゆる嫌がらせや誹謗中傷、反社会的行為を含む発表はお断りします。 応募内容に含まれる個人情報は、JANOG58 プログラム募集目的で使用します。 ご応募をいただいた時点で、JANOG における個人情報取扱ポリシー に同意いただいたものとします。 QA Q.なぜ最大7人なのですか？ A.75分を7で割ると1人当たり10分となります。この時QAの時間の目安を3分としているのでプレゼン時間は7分となります。 Q.7人以下の場合はどうなりますか？ A.持ち時間は人数で割ることになります。２人の場合は１人あたり 持ち時間32分となります。 Q.人数が少なく、短い話なので時間を使い切れない時はどうなりますか？ A.ゆっくりと質疑をもうける事になります。また司会の裁量により登壇を会場に募る事も考えられます。その時は登壇7分QA３分の10分の持ちタイムで実施してもらいます。 Q.採用はいつわかりますか？ A.採点基準に達した場合は即時に採用通知を送らせて頂きます。未達の場合は採用期間終了後にご連絡させて頂きます。 Q.応募資料から登壇資料の変更は可能ですか？ A.前日まで自身の登壇時間が分からない為、変更は可能とさせて頂きます。ただし応募資料のコンセプトは維持して頂く様にお願いします。 Q.ストリーミングやアーカイブはされますか？ A.されません。 Q.資料は公開されますか？ A.応募資料、発表資料のいずれか、もしくは両方を公開させて頂きます。

### JANOG Update + オープンマイク
本セッションではJANOGの運営について会場のみなさまとディスカッションする時間を設けます。 イメージとしてはIETFのIABオープンマイク、IAOCオープンマイクのような形態を想定しています。 はじめに通常のJANOG updateのご報告をして、その後運営委員が登壇し、会場のみなさんからご質問やご意見・ご提案をいただきます。 ミーティング運営の在り方、他コミュニティとの連携、JANOGが価値ある団体でいるためにどういう活動をすべきか、JANOGとして必要な機能、などざっくばらんに話し合う時間にしたいと考えています。

### 閉会宣言 / 次回開催予告
slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/JANOG58_閉会宣言.pdf | slides: https://www.janog.gr.jp/meeting/janog58/wp-content/uploads/2026/05/次回予告_20260716.pdf
閉会宣言/次回開催予告

