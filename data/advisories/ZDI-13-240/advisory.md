# ZDI-13-240: Hewlett-Packard Intelligent Management Center SOM euAccountService Servlet Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-240
- **ZDI-CAN:** ZDI-CAN-1644
- **Date:** 2013-10-16
- **CVE:** CVE-2013-4824
- **CVSS:** 9.4
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:N
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Intelligent Management Center
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-240/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP Intelligent Management Center. Authentication is not required to exploit this vulnerability. The specific flaw exists within the SOM's euAccountService servlet. No authentication is required to take advantage of this vulnerability, which allows the creation of a web administration account. An attacker can leverage this to manipulate other devices and users managed by the application and possibly leverage this situation to achieve remote code execution.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03943547

## Disclosure Timeline

- 2012-11-19 - Vulnerability reported to vendor
- 2013-10-16 - Coordinated public release of advisory
