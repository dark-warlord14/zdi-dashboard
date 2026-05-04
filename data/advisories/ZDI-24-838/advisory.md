# ZDI-24-838: (Pwn2Own) Wyze Cam v3 Wi-Fi SSID OS Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-838
- **ZDI-CAN:** ZDI-CAN-22337
- **Date:** 2024-06-21
- **CVE:** CVE-2024-6247
- **CVSS:** 6.8
- **CVSS Vector:** AV:P/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Wyze
- **Affected Products:** Cam v3
- **Credit:** Stefan Schiller (Sonar)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-838/
## Vulnerability Details

This vulnerability allows physically present attackers to execute arbitrary code on affected installations of Wyze Cam v3 IP cameras. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of SSIDs embedded in scanned QR codes. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Wyze has issued an update to correct this vulnerability. More details can be found at: https://forums.wyze.com/t/security-advisory/289256

## Disclosure Timeline

- 2023-11-09 - Vulnerability reported to vendor
- 2024-06-21 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
