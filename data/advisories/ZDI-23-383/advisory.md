# ZDI-23-383: Microsoft Windows Bluetooth BNEP Protocol Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-383
- **ZDI-CAN:** ZDI-CAN-20475
- **Date:** 2023-04-11
- **CVE:** CVE-2023-28227
- **CVSS:** 7.6
- **CVSS Vector:** AV:A/AC:H/PR:L/UI:R/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-383/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must connect a malicious Bluetooth device. The specific flaw exists within the processing of BNEP packets. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the kernel.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-28227

## Disclosure Timeline

- 2023-03-10 - Vulnerability reported to vendor
- 2023-04-11 - Coordinated public release of advisory
