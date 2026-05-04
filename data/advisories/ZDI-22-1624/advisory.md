# ZDI-22-1624: Microsoft Exchange PowerShell Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1624
- **ZDI-CAN:** ZDI-CAN-18333
- **Date:** 2022-10-17
- **CVE:** CVE-2022-41082
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Exchange
- **Credit:** DA-0x43-Dx4-DA-Hx2-Tx2-TP-S-Q from GTSC
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1624/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Exchange. Authentication is required to exploit this vulnerability. The specific flaw exists within the PowerShell endpoint. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-41082

## Disclosure Timeline

- 2022-10-20 - Vulnerability reported to vendor
- 2022-10-17 - Coordinated public release of advisory
- 2022-11-22 - Advisory Updated
