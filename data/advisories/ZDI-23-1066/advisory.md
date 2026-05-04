# ZDI-23-1066: Microsoft Windows Bluetooth AVDTP Protocol Integer Underflow Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1066
- **ZDI-CAN:** ZDI-CAN-20988
- **Date:** 2023-08-14
- **CVE:** CVE-2023-35387
- **CVSS:** 6.2
- **CVSS Vector:** AV:A/AC:H/PR:L/UI:R/S:C/C:L/I:N/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Lucas Leong (@_wmliang_) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1066/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to disclose sensitive information on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must connect a malicious Bluetooth device. The specific flaw exists within the processing of AVDTP commands. The issue results from the lack of proper validation of user-supplied data, which can result in an integer underflow before reading from memory. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the kernel.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-35387

## Disclosure Timeline

- 2023-05-01 - Vulnerability reported to vendor
- 2023-08-14 - Coordinated public release of advisory
