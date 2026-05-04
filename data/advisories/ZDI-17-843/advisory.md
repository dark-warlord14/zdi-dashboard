# ZDI-17-843: Microsoft Windows SMB Out-Of-Bounds Read Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-843
- **ZDI-CAN:** ZDI-CAN-5069
- **Date:** 2017-10-10
- **CVE:** CVE-2017-11781
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:L/Au:S/C:N/I:N/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** pesante
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-843/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service on vulnerable installations of Microsoft Windows. Authentication is required to exploit this vulnerability, assuming the product is in its default configuration. The specific flaw exists within the srv driver. A crafted request to an SMB share can trigger a read past the end of an allocated buffer. An attacker can leverage this vulnerability to create a denial-of-service condition to users of the system.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-11781

## Disclosure Timeline

- 2017-07-27 - Vulnerability reported to vendor
- 2017-10-10 - Coordinated public release of advisory
