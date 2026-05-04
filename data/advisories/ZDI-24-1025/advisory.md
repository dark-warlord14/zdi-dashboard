# ZDI-24-1025: NI VeriStand IFileTransferServer Exposed Dangerous Method Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1025
- **ZDI-CAN:** ZDI-CAN-22070
- **Date:** 2024-07-30
- **CVE:** CVE-2024-6805
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** NI
- **Affected Products:** VeriStand
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1025/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of NI VeriStand. Authentication is not required to exploit this vulnerability. The specific flaw exists within the IFileTransferServer component. The issue results from an exposed dangerous method. An attacker can leverage this vulnerability to disclose information in the context of the current user.

## Additional Details

NI has issued an update to correct this vulnerability. More details can be found at: https://www.ni.com/en/support/security/available-critical-and-security-updates-for-ni-software/missing-authorization-checks-in-ni-veristand-gateway.html

## Disclosure Timeline

- 2024-03-27 - Vulnerability reported to vendor
- 2024-07-30 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
