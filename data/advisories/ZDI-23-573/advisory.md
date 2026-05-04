# ZDI-23-573: Microsoft Windows PE Parsing Integer Overflow Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-573
- **ZDI-CAN:** ZDI-CAN-20044
- **Date:** 2023-05-10
- **CVE:** CVE-2023-24949
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-573/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of relocation tables in PE files. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow when performing a bounds check before reading from memory. An attacker can leverage this vulnerability to create a persistent denial-of-service condition on the system.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-24949

## Disclosure Timeline

- 2023-02-08 - Vulnerability reported to vendor
- 2023-05-10 - Coordinated public release of advisory
