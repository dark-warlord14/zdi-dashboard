# ZDI-24-1129: Magnet Forensics AXIOM Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1129
- **ZDI-CAN:** ZDI-CAN-23964
- **Date:** 2024-08-13
- **CVE:** CVE-2024-7448
- **CVSS:** 8.0
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Magnet Forensics
- **Affected Products:** AXIOM
- **Credit:** Andrew Clark IV
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1129/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Magnet Forensics AXIOM. User interaction is required to exploit this vulnerability in that the target must acquire data from a malicious mobile device. The specific flaw exists within the Android device image acquisition functionality. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Magnet Forensics has issued an update to correct this vulnerability. More details can be found at: https://docs.magnetforensics.com/docs/axiom/release_notes.html

## Disclosure Timeline

- 2024-06-05 - Vulnerability reported to vendor
- 2024-08-13 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
