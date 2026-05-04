# ZDI-23-1533: Magnet Forensics AXIOM Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1533
- **ZDI-CAN:** ZDI-CAN-21255
- **Date:** 2023-10-06
- **CVE:** CVE-2023-42128
- **CVSS:** 8.0
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Magnet Forensics
- **Affected Products:** AXIOM
- **Credit:** Andrew Clark IV
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1533/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Magnet Forensics AXIOM. User interaction is required to exploit this vulnerability in that the target must acquire data from a malicious mobile device. The specific flaw exists within the Android device image acquisition functionality. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Fixed in AXIOM v7.6

## Disclosure Timeline

- 2023-09-05 - Vulnerability reported to vendor
- 2023-10-06 - Coordinated public release of advisory
