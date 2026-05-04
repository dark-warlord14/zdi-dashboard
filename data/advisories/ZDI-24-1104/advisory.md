# ZDI-24-1104: Logsign Unified SecOps Platform Incorrect Authorization Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1104
- **ZDI-CAN:** ZDI-CAN-25029
- **Date:** 2024-08-08
- **CVE:** CVE-2024-7604
- **CVSS:** 5.1
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:N
- **Affected Vendors:** Logsign
- **Affected Products:** Unified SecOps Platform
- **Credit:** Smile Thanapattheerakul of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1104/
## Vulnerability Details

This vulnerability allows local attackers to bypass authentication on affected installations of Logsign Unified SecOps Platform. Authentication is required to exploit this vulnerability. The specific flaw exists within the HTTP API service, which listens on TCP port 443 by default. The issue results from the lack of proper validation of the user's license expiration date. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Logsign has issued an update to correct this vulnerability. More details can be found at: https://support.logsign.net/hc/en-us/articles/20617133769362-06-08-2024-Version-6-4-23-Release-Notes

## Disclosure Timeline

- 2024-08-06 - Vulnerability reported to vendor
- 2024-08-08 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
