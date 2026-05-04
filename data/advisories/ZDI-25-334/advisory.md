# ZDI-25-334: Microsoft Windows Remote Desktop Gateway Service Null Pointer Dereference Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-334
- **ZDI-CAN:** ZDI-CAN-26776
- **Date:** 2025-06-10
- **CVE:** CVE-2025-30394
- **CVSS:** 8.6
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:C/C:N/I:N/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-334/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Microsoft Windows. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Remote Desktop Gateway service. The issue results from dereferencing a null pointer. An attacker can leverage this vulnerability to create a denial of service condition on remote desktop hosts behind the gateway.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-30394

## Disclosure Timeline

- 2025-05-02 - Vulnerability reported to vendor
- 2025-06-10 - Coordinated public release of advisory
- 2025-06-10 - Advisory Updated
