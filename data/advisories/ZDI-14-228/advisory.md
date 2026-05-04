# ZDI-14-228: Hewlett-Packard SiteScope EmailServlet servlet Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-228
- **ZDI-CAN:** ZDI-CAN-2140
- **Date:** 2014-07-09
- **CVE:** CVE-2014-2614
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** SiteScope
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-228/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett-Packard SiteScope. Authentication is not required to exploit this vulnerability. The specific flaw exists within the EmailServlet servlet. The issue lies in the ability to download arbitrary files. A remote attacker can abuse this to disclose sensitive information that could result in remote code execution under the context of the process.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c04355129

## Disclosure Timeline

- 2014-03-07 - Vulnerability reported to vendor
- 2014-07-09 - Coordinated public release of advisory
