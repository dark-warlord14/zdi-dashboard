# ZDI-22-384: Microsoft Office Visio EMF EMR_DELETEOBJECT Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-384
- **ZDI-CAN:** ZDI-CAN-15731
- **Date:** 2022-02-18
- **CVE:** CVE-2022-21988
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Visio
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-384/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Office Visio. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of EMR_DELETEOBJECT records in EMF images. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-21988

## Disclosure Timeline

- 2021-11-10 - Vulnerability reported to vendor
- 2022-02-18 - Coordinated public release of advisory
