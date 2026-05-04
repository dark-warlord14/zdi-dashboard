# ZDI-25-745: (Pwn2Own) QNAP TS-464 reset_password.cgi Improper Certificate Validation Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-745
- **ZDI-CAN:** ZDI-CAN-25644
- **Date:** 2025-07-31
- **CVE:** N/A
- **CVSS:** 5.3
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** QNAP
- **Affected Products:** TS-464
- **Credit:** @quangnh89 and @ExLuck99
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-745/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to disclose sensitive information on affected installations of QNAP TS-464 devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the reset_password.cgi endpoint. The issue results from the lack of proper validation of the certificate presented by a server. An attacker can leverage this vulnerability to disclose information in the context of the device.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/en-us/security-advisories

## Disclosure Timeline

- 2024-12-02 - Vulnerability reported to vendor
- 2025-07-31 - Coordinated public release of advisory
- 2025-07-31 - Advisory Updated
