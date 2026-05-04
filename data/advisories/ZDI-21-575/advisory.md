# ZDI-21-575: Microsoft Excel XLS File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-575
- **ZDI-CAN:** ZDI-CAN-12934
- **Date:** 2021-05-13
- **CVE:** CVE-2021-31176
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Excel
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-575/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Excel. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of XLS files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-31176

## Disclosure Timeline

- 2021-02-26 - Vulnerability reported to vendor
- 2021-05-13 - Coordinated public release of advisory
