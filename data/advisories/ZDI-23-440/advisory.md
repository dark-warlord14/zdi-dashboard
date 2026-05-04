# ZDI-23-440: Linux Kernel DPT I2O Controller Time-Of-Check Time-Of-Use Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-440
- **ZDI-CAN:** ZDI-CAN-17016
- **Date:** 2023-04-13
- **CVE:** CVE-2023-2007
- **CVSS:** 6.7
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:N/A:L
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Lucas Leong (@_wmliang_) and Reno Robert of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-440/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Linux Kernel. An attacker must first obtain the ability to execute high-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the DPT I2O Controller driver. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://github.com/torvalds/linux/commit/b04e75a4a8a81887386a0d2dbf605a48e779d2a0

## Disclosure Timeline

- 2022-04-01 - Vulnerability reported to vendor
- 2023-04-13 - Coordinated public release of advisory
