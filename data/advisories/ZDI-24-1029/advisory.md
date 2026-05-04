# ZDI-24-1029: NI VeriStand DataLoggingServer Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1029
- **ZDI-CAN:** ZDI-CAN-22068
- **Date:** 2024-07-30
- **CVE:** CVE-2024-6793
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NI
- **Affected Products:** VeriStand
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1029/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of NI VeriStand. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of service requests in the DataLoggingServer component. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

NI has issued an update to correct this vulnerability. More details can be found at: https://www.ni.com/en/support/security/available-critical-and-security-updates-for-ni-software/deserialization-of-untrusted-data-vulnerabilities-in-ni-veristand.html

## Disclosure Timeline

- 2024-03-13 - Vulnerability reported to vendor
- 2024-07-30 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
