# ZDI-14-234: Hewlett-Packard Intelligent Management Center IctDownloadServlet Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-234
- **ZDI-CAN:** ZDI-CAN-2090
- **Date:** 2014-07-16
- **CVE:** CVE-2014-2621
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Intelligent Management Center
- **Credit:** Bluesea
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-234/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett-Packard Intelligent Management Center. Authentication is not required to exploit this vulnerability. The specific flaw exists within the IctDownloadServlet servlet. This servlet contains a directory traversal issue which allows any file readable by SYSTEM to be disclosed. By abusing this behavior, an attacker can disclose administrative credentials and possibly leverage this situation to achieve remote code execution.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/template.PAGE/public/kb/docDisplay/?spf_p.tpst=kbDocDisplay&spf_p.prp_kbDocDisplay=wsrp-navigationalState%3DdocId%253Demr_na-c04369484-1%257CdocLocale%253D%257CcalledBy%253D&javax.portlet.begCacheTok=com.vignette.cachetoken&javax.portlet.endCacheTok=com.vignette.cachetoken

## Disclosure Timeline

- 2013-12-18 - Vulnerability reported to vendor
- 2014-07-16 - Coordinated public release of advisory
