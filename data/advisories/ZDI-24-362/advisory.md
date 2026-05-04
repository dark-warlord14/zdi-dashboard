# ZDI-24-362: Microsoft Azure Private 5G Core InitialUEMessage Improper Input Validation Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-362
- **ZDI-CAN:** ZDI-CAN-23397
- **Date:** 2024-04-09
- **CVE:** CVE-2024-20685
- **CVSS:** 5.9
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Azure
- **Credit:** Salim S.I, Richard Y Lin, Atlas Huang (CTOne/TrendMicro)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-362/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Microsoft Azure Private 5G Core. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of InitialUEMessage messages. The issue results from improper length validation. An attacker can leverage this vulnerability to create a denial-of-service condition on the 5G network.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-20685

## Disclosure Timeline

- 2024-03-07 - Vulnerability reported to vendor
- 2024-04-09 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
