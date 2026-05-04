# ZDI-24-439: Microsoft Windows Bluetooth AVDTP Protocol Integer Underflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-439
- **ZDI-CAN:** ZDI-CAN-20464
- **Date:** 2024-05-09
- **CVE:** CVE-2023-24948
- **CVSS:** 7.6
- **CVSS Vector:** AV:A/AC:H/PR:L/UI:R/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-439/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must connect a malicious Bluetooth device. The specific flaw exists within the processing of AVDTP packets. The issue results from the lack of proper validation of user-supplied data, which can result in an integer underflow before writing to memory. An attacker can leverage this vulnerability to execute code in the context of the kernel.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-24948

## Disclosure Timeline

- 2023-03-10 - Vulnerability reported to vendor
- 2024-05-09 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
