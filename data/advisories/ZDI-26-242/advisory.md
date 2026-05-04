# ZDI-26-242: (Pwn2Own) QNAP TS-453E server_handlers.pyc rr2s.kwargs Error Message Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-242
- **ZDI-CAN:** ZDI-CAN-28426
- **Date:** 2026-03-30
- **CVE:** CVE-2025-62840
- **CVSS:** 3.5
- **CVSS Vector:** AV:A/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** QNAP
- **Affected Products:** TS-453E
- **Credit:** Bongeun Koo (@kiddo_pwn) and Evangelos Daravigkas (@freddo_1337) of Team DDOS
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-242/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to disclose sensitive information on affected installations of QNAP TS-453E devices. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the handling of the rr2s.kwargs parameter provided to the server_handlers.pyc endpoint. The issue results from outputting an error message that includes sensitive information. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the RR2 administrator.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/en/security-advisory/qsa-25-46

## Disclosure Timeline

- 2025-11-18 - Vulnerability reported to vendor
- 2026-03-30 - Coordinated public release of advisory
- 2026-03-30 - Advisory Updated
