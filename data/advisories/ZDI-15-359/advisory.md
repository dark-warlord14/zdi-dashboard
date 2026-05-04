# ZDI-15-359: (0Day) (Mobile Pwn2Own) Microsoft Internet Explorer CTableLayout::AddRow Out-Of-Bounds Memory Access Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-359
- **ZDI-CAN:** ZDI-CAN-2619
- **Date:** 2015-07-20
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer Mobile
- **Credit:** Nicolas Joly
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-359/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer, including on Windows Phone. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to how Internet Explorer processes arrays representing cells in HTML tables. By manipulating a document's elements an attacker can force a Internet Explorer to use memory past the end of an array of HTML cells. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 11/12/2014 - ZDI disclosed the case to the vendor at Mobile Pwn2Own 02/23/2015 - ZDI asked the vendor if an extension was needed 03/05/2015 - The vendor requested an extension to 07/19/2015 (to match with a couple of similar cases) 03/05/2015 - ZDI agreed to extend out to 05/12/2015 03/23/2015 - The vendor wrote to ensure the case was extended to 05/13/2015 - ZDI agreed 04/29/2015 - ZDI requested a status update 04/30/2015 - The vendor notified ZDI that they would not meet the new deadline ZDI decided to wait out the original extension request to 07/19/2015 (to match with a couple of similar cases) 07/02/2015 and 07/06/2015 - ZDI requested a status update 07/06/2015 - The vendor replied with an expected build, but not a date 07/06/2015 - ZDI notified of the intent to 0-day the week of 07/20/2015 -- Mitigation: - In a web-based attack scenario, an attacker could host a specially crafted website that is designed to exploit these vulnerabilities through Internet Explorer, and then convince a user to view the website. The attacker could also take advantage of compromised websites and websites that accept or host user-provided content or advertisements. These websites could contain specially crafted content that could exploit these vulnerabilities. In all cases, however, an attacker would have no way to force users to view the attacker-controlled content. Instead, an attacker would have to convince users to take action, typically by getting them to click a link in an email message or in an Instant Messenger message that takes users to the attacker's website, or by getting them to open an attachment sent through email. - Configure Internet Explorer to prompt before running Active Scripting or to disable Active Scripting in the Internet and Local intranet security zone

## Disclosure Timeline

- 2014-11-12 - Vulnerability reported to vendor
- 2015-07-20 - Coordinated public release of advisory
