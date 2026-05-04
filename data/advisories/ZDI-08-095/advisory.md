# ZDI-08-095: EMC ApplicationXtender Workflow Server Admin Agent Arbitrary File Upload Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-095
- **ZDI-CAN:** ZDI-CAN-358
- **Date:** 2008-08-14
- **CVE:** CVE-2008-3685
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** EMC
- **Affected Products:** ApplicationXtender Workflow
- **Credit:** Stephen Fewer of Harmony Security (www.harmonysecurity.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-095/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on systems with vulnerable installations of EMC ApplicationXtender Workflow Server. Authentication is not required to exploit this vulnerability. The specific flaw exists in the Admin Agent service (aws_tmxn.exe) which listens by default on TCP port 2606. The process exposes functionality to upload arbitrary files to the remote system. The daemon fails to sanitize directory traversal attacks, allowing remote attackers to overwrite critical system files or even the Admin Agent executable itself. Exploitation allows for arbitrary code execution under the context of the SYSTEM user.

## Additional Details

Both issues have been addressed by a hotfix available from EMC AX Support. To obtain the hot fix contact EMC AX Support at 1-877-534-2867 and reference EMC AX Support issue CQOTG00074151

## Disclosure Timeline

- 2008-07-07 - Vulnerability reported to vendor
- 2008-08-14 - Coordinated public release of advisory
