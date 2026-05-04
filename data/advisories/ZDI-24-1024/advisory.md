# ZDI-24-1024: NI VeriStand ProjectServer Exposed Dangerous Method Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1024
- **ZDI-CAN:** ZDI-CAN-22167
- **Date:** 2024-07-30
- **CVE:** CVE-2024-6805
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** NI
- **Affected Products:** VeriStand
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1024/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of NI VeriStand. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of service requests in the ProjectServer component. The issue results from an exposed dangerous method. An attacker can leverage this vulnerability to create a denial-of-service condition on the VeriStand system.

## Additional Details

NI has issued an update to correct this vulnerability. More details can be found at: https://www.ni.com/en/support/security/available-critical-and-security-updates-for-ni-software/missing-authorization-checks-in-ni-veristand-gateway.html

## Disclosure Timeline

- 2024-03-08 - Vulnerability reported to vendor
- 2024-07-30 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
