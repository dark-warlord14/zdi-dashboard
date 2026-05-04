# ZDI-25-256: Avast Free Antivirus Integer Overflow Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-256
- **ZDI-CAN:** ZDI-CAN-26610
- **Date:** 2025-04-24
- **CVE:** CVE-2025-3500
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Avast
- **Affected Products:** Free Antivirus
- **Credit:** Baris Akkaya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-256/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Avast Free Antivirus. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the aswbidsdriver kernel driver. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Fixed in Version 25.3.9983.922

## Disclosure Timeline

- 2025-04-02 - Vulnerability reported to vendor
- 2025-04-24 - Coordinated public release of advisory
- 2025-04-24 - Advisory Updated
