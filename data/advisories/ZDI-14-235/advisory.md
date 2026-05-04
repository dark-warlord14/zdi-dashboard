# ZDI-14-235: Hewlett-Packard Intelligent Management Center RssServlet Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-235
- **ZDI-CAN:** ZDI-CAN-2312
- **Date:** 2014-07-16
- **CVE:** CVE-2014-2622
- **CVSS:** 8.5
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:N
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Intelligent Management Center
- **Credit:** Brandon Perry
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-235/
## Vulnerability Details

This vulnerability allows remote attackers to obtain sensitive information on vulnerable installations of Hewlett-Packard Intelligent Management Center. Authentication is required to exploit this vulnerability. The specific flaw exists within the RssServlet servlet. This servlet exhibits an XML external entity injection vulnerability which allows any file readable by SYSTEM to be disclosed. By abusing this behavior an attacker can disclose administrative credentials and possibly leverage this situation to achieve remote code execution.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/template.PAGE/public/kb/docDisplay/?spf_p.tpst=kbDocDisplay&spf_p.prp_kbDocDisplay=wsrp-navigationalState%3DdocId%253Demr_na-c04369484-1%257CdocLocale%253D%257CcalledBy%253D&javax.portlet.begCacheTok=com.vignette.cachetoken&javax.portlet.endCacheTok=com.vignette.cachetoken

## Disclosure Timeline

- 2014-05-02 - Vulnerability reported to vendor
- 2014-07-16 - Coordinated public release of advisory
