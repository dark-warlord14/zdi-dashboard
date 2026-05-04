# ZDI-15-240: Dell NetVault Backup Heap Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-240
- **ZDI-CAN:** ZDI-CAN-2606
- **Date:** 2015-05-26
- **CVE:** CVE-2015-4067
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Dell
- **Affected Products:** NetVault Backup
- **Credit:** sztivi
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-240/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Dell NetVault Backup. Authentication is not required to exploit this vulnerability. The specific flaw exists within the libnv6 module. By manipulating a serialized object's template string specifiers, an attacker can cause an integer overflow resulting in an undersized allocation and eventually a heap overflow. An attacker can leverage this vulnerability to execute code under the context of SYSTEM.

## Additional Details

Dell has issued an update to correct this vulnerability. More details can be found at: http://documents.software.dell.com/netvault-backup/10.0.5/release-notes/

## Disclosure Timeline

- 2015-02-05 - Vulnerability reported to vendor
- 2015-05-26 - Coordinated public release of advisory
