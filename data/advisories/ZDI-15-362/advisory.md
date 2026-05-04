# ZDI-15-362: (0Day) Microsoft Internet Explorer CTreePos Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-362
- **ZDI-CAN:** ZDI-CAN-2695
- **Date:** 2015-07-20
- **CVE:** N/A
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer Mobile
- **Credit:** AbdulAziz Hariri - HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-362/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of CTreePos objects. By manipulating a document's elements an attacker can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 01/20/15 - ZDI disclosed to the vendor 01/20/15 - The vendor acknowledged 3/5/2015 - The vendor requested an extension to 07/19/2015 3/5/2015 - ZDI agreed to an extension to 07/19/2015 07/02/2015 and 07/06/2015 - ZDI requested a status update 07/06/2015 - The vendor replied with an expected build, but not a date 07/06/2015 - ZDI notified of the intent to 0-day the week of 07/20/2015 -- Mitigation: - In a web-based attack scenario, an attacker could host a specially crafted website that is designed to exploit these vulnerabilities through Internet Explorer, and then convince a user to view the website. The attacker could also take advantage of compromised websites and websites that accept or host user-provided content or advertisements. These websites could contain specially crafted content that could exploit these vulnerabilities. In all cases, however, an attacker would have no way to force users to view the attacker-controlled content. Instead, an attacker would have to convince users to take action, typically by getting them to click a link in an email message or in an Instant Messenger message that takes users to the attacker's website, or by getting them to open an attachment sent through email. - Configure Internet Explorer to prompt before running Active Scripting or to disable Active Scripting in the Internet and Local intranet security zone

## Disclosure Timeline

- 2015-01-20 - Vulnerability reported to vendor
- 2015-07-20 - Coordinated public release of advisory
