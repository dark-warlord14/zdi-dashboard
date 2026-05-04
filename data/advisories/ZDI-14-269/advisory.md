# ZDI-14-269: Attachmate Verastream Process Designer Process Server Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-269
- **ZDI-CAN:** ZDI-CAN-2161
- **Date:** 2014-07-30
- **CVE:** CVE-2014-0607
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Attachmate
- **Affected Products:** Verastream Process Designer
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-269/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Attachmate Verastream Process Designer. Authentication is not required to exploit this vulnerability. The specific flaw exists within the 'DeploymentService' Axis web service. This web service is not protected by authentication requirements and suffers from a directory traversal vulnerability. By sending a specially crafted SOAP request, it is possible to upload files into the web server's root directory. A remote attacker can abuse this to execute remote code under the context of SYSTEM.

## Additional Details

Attachmate has issued an update to correct this vulnerability. More details can be found at: http://support.attachmate.com/techdocs/2700.html

## Disclosure Timeline

- 2014-05-02 - Vulnerability reported to vendor
- 2014-07-30 - Coordinated public release of advisory
