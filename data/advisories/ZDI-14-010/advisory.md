# ZDI-14-010: HP Application Information Optimizer DataDirect OpenAccess GIOP Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-010
- **ZDI-CAN:** ZDI-CAN-1666
- **Date:** 2014-01-29
- **CVE:** CVE-2013-6189
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Application Information Optimizer
- **Credit:** Aniway.Anyway@gmail.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-010/
## Vulnerability Details

This vulnerability potentially allows remote attackers to execute arbitrary code on vulnerable installations of HP Application Information Optimizer. Authentication is not required to exploit this vulnerability. The specific flaw exists within oasoa.exe which listens by default on port 19988. A stack-based vulnerability can be triggered when a certain opcode byte is not in the right range. Arbitrary data can be copied to the stack and an attacker may be able to leverage this vulnerability into remote execution of arbitrary code as SYSTEM.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: http://h20565.www2.hp.com/portal/site/hpsc/template.PAGE/public/kb/docDisplay/?spf_p.tpst=kbDocDisplay&spf_p.prp_kbDocDisplay=wsrp-navigationalState%3DdocId%253Demr_na-c04041078-1%257CdocLocale%253D%257CcalledBy%253D&javax.portlet.begCacheTok=com.vignette.cachetoken&javax.portlet.endCacheTok=com.vignette.cachetoken

## Disclosure Timeline

- 2013-05-14 - Vulnerability reported to vendor
- 2014-01-29 - Coordinated public release of advisory
