# ZDI-12-015: (0Day) HP StorageWorks P2000 G3 Directory Traversal and Default Account Vulnerabilities

## Metadata

- **ZDI ID:** ZDI-12-015
- **ZDI-CAN:** ZDI-CAN-1243
- **Date:** 2012-01-12
- **CVE:** CVE-2011-4788
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:P/A:P
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** StorageWorks P2000 G3
- **Credit:** Carlos Perez at Tenable Network Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-015/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP MSA 2000 G3. Authentication is not required to exploit this vulnerability. The specific flaws exists within the web interface listening on TCP port 80. There exists a directory traversal flaw that can allow a remote attacker to view any file on the system by simply specifying it in the default URI. Additionally, the pasword file contains a default login that can be used to authenticate to the device. This can be leveraged by a remote attacker to perform any tasks an administrator is able to.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 180 day deadline. -- Mitigation: HP states that a patch for this vulnerability will be made available to the public "soon." Until that time, it is recommended that administrators of StorageWorks systems restrict access to the web interface on 80/tcp to authorized hosts only.

## Disclosure Timeline

- 2011-06-01 - Vulnerability reported to vendor
- 2012-01-12 - Coordinated public release of advisory
