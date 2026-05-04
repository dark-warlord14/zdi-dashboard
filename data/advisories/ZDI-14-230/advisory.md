# ZDI-14-230: Hewlett-Packard Universal CMDB Default Credentials Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-230
- **ZDI-CAN:** ZDI-CAN-2104
- **Date:** 2014-07-09
- **CVE:** CVE-2014-2617
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Universal CMDB
- **Credit:** Ziad Badawi
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-230/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett-Packard Universal CMDB. Authentication is not required to exploit this vulnerability. The specific flaw exists within the default configuration of Hewlett-Packard Universal CMDB. The configuration contains hard-coded credentials. An attacker can leverage this vulnerability to upload malicious applications that can then be used to execute code under the context of SYSTEM.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c04357076

## Disclosure Timeline

- 2014-03-07 - Vulnerability reported to vendor
- 2014-07-09 - Coordinated public release of advisory
