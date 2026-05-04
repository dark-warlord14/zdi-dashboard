# ZDI-14-343: Hewlett-Packard Network Node Manager ovopi.dll Command 685 Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-343
- **ZDI-CAN:** ZDI-CAN-2373
- **Date:** 2014-10-01
- **CVE:** CVE-2014-2624
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Network Node Manager
- **Credit:** sztivi
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-343/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett-Packard Network Node Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within ovopi.dll which listens by default on UDP port 696. When parsing command number 685, the process blindly copies user supplied data which can be used to overwrite a vtable or any arbitrary address. A remote attacker can abuse this to execute remote code under the context of the SYSTEM user.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20565.www2.hp.com/portal/site/hpsc/template.PAGE/public/kb/docDisplay/?spf_p.tpst=kbDocDisplay&spf_p.prp_kbDocDisplay=wsrp-navigationalState%3DdocId%253Demr_na-c04378450-2%257CdocLocale%253D%257CcalledBy%253D&

## Disclosure Timeline

- 2014-07-24 - Vulnerability reported to vendor
- 2014-10-01 - Coordinated public release of advisory
