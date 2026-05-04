# ZDI-25-740: (Pwn2Own) QNAP QHora-322 backup Use of Hard-coded Cryptographic Key Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-740
- **ZDI-CAN:** ZDI-CAN-25641
- **Date:** 2025-07-31
- **CVE:** N/A
- **CVSS:** 8.0
- **CVSS Vector:** AV:A/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** QNAP
- **Affected Products:** QHora-322
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-740/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of QNAP QHora-322 routers. Authentication is required to exploit this vulnerability. The specific flaw exists within the Backup and Restore functionality. The issue results from the use of a hardcoded cryptographic key. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/en-us/security-advisories

## Disclosure Timeline

- 2024-12-02 - Vulnerability reported to vendor
- 2025-07-31 - Coordinated public release of advisory
- 2025-07-31 - Advisory Updated
