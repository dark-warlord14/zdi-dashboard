# ZDI-13-263: HP SiteScope issueSiebelCmd SOAP Request Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-263
- **ZDI-CAN:** ZDI-CAN-1765
- **Date:** 2013-11-24
- **CVE:** CVE-2013-4835
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** SiteScope
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-263/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP SiteScope. Authentication is not required to exploit this vulnerability. The specific flaw exists within the issueSiebelCmd() web method. A remote attacker can abuse this web method in order to remotely execute code under the context of the SYSTEM user.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03969435

## Disclosure Timeline

- 2013-02-22 - Vulnerability reported to vendor
- 2013-11-24 - Coordinated public release of advisory
