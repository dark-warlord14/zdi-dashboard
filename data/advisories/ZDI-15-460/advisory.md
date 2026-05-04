# ZDI-15-460: Solarwinds Storage Manager ProcessFileUpload.jsp File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-460
- **ZDI-CAN:** ZDI-CAN-2731
- **Date:** 2015-10-07
- **CVE:** CVE-2015-7838
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** SolarWinds
- **Affected Products:** Storage Manager
- **Credit:** Matt Molinyawe - HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-460/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Solarwinds Storage Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within ProcessFileUpload.jsp within the handling of file uploads. The issue lies in the failure to sanitize the files uploaded, allowing them to be placed within directories accessible through the service. An attacker can leverage this vulnerability to execute code as SYSTEM.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: http://www.solarwinds.com/documentation/srm/docs/releasenotes/releasenotes.htm

## Disclosure Timeline

- 2015-02-04 - Vulnerability reported to vendor
- 2015-10-07 - Coordinated public release of advisory
