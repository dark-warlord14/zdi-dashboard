# ZDI-05-001: VERITAS NetBackup Remote Code Execution

## Metadata

- **ZDI ID:** ZDI-05-001
- **ZDI-CAN:** ZDI-CAN-001
- **Date:** 2005-10-12
- **CVE:** CVE-2005-2715
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Symantec
- **Affected Products:** Veritas NetBackup
- **Credit:** This vulnerability was discovered by Kevin Finisterre with exploitation assistance from JohnH.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-05-001/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable NetBackup installations. Authentication is not required to exploit this vulnerability. This specific flaw exists within the bpjava-msvc daemon due to incorrect handling of format string data passed through the 'COMMAND_LOGON_TO_MSERVER' command. The vulnerable daemon listens on TCP port 13722 and affects both NetBackup clients and servers.

## Additional Details

Symantec Engineers have verified this issue and made security updates available for the supported VERITAS NetBackup products. Symantec strongly recommends all customers immediately apply the latest updates for their supported product versions to protect against these types of threats. Please refer to the Symantec advisory for update information: http://www.symantec.com/avcenter/security/Content/2005.10.12.html

## Disclosure Timeline

- 2005-09-12 - Vulnerability reported to vendor
- 2005-10-12 - Coordinated public release of advisory
