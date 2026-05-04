# ZDI-14-043: Hewlett-Packard SiteScope SOAP Arbitrary File Download and Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-043
- **ZDI-CAN:** ZDI-CAN-2084
- **Date:** 2014-04-03
- **CVE:** CVE-2013-6207
- **CVSS:** 9.4
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:N/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** SiteScope
- **Credit:** Mike Arnold (Bruk0ut)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-043/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett-Packard SiteScope. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of SOAP requests. The issue lies in failure to require authentication to several SOAP endpoints. By taking advantage of this behavior, an attacker can shutdown the service or disclose administrative credentials and possibly leverage this situation to achieve remote code execution.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03969435

## Disclosure Timeline

- 2014-02-16 - Vulnerability reported to vendor
- 2014-04-03 - Coordinated public release of advisory
