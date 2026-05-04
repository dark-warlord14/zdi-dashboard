# ZDI-08-096: EMC ApplicationXtender Workflow Server Admin Agent Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-096
- **ZDI-CAN:** ZDI-CAN-360
- **Date:** 2008-08-14
- **CVE:** CVE-2008-3684
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** EMC
- **Affected Products:** ApplicationXtender Workflow
- **Credit:** Stephen Fewer of Harmony Security (www.harmonysecurity.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-096/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on systems with vulnerable installations of EMC ApplicationXtender Workflow Server. Authentication is not required to exploit this vulnerability. The specific flaw exists in the Admin Agent service (aws_tmxn.exe) which listens by default on TCP port 2606. The process receives network packet data into a static heap buffer. Exploitation allows remote attackers to corrupt heap memory subsequently leading to arbitrary code execution under the context of the SYSTEM user.

## Additional Details

Both issues have been addressed by a hotfix available from EMC AX Support. To obtain the hot fix contact EMC AX Support at 1-877-534-2867 and reference EMC AX Support issue CQOTG00074151

## Disclosure Timeline

- 2008-07-07 - Vulnerability reported to vendor
- 2008-08-14 - Coordinated public release of advisory
