# ZDI-21-577: Microsoft Windows win32kfull Font Entry Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-577
- **ZDI-CAN:** ZDI-CAN-13320
- **Date:** 2021-05-13
- **CVE:** CVE-2021-31188
- **CVSS:** 6.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Lucas Leong (@_wmliang_) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-577/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of Font Entry objects. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-31188

## Disclosure Timeline

- 2021-03-03 - Vulnerability reported to vendor
- 2021-05-13 - Coordinated public release of advisory
