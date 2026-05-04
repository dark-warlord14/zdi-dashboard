# ZDI-09-101: Novell ZENworks Desktop Management Installation Service Remote Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-101
- **ZDI-CAN:** ZDI-CAN-450
- **Date:** 2009-11-30
- **CVE:** N/A
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Novell
- **Affected Products:** Zenworks
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-101/
## Vulnerability Details

This vulnerability allows remote attackers to impersonate valid users in vulnerable installations of Novell ZENworks Desktop Management. Authentication is not required to exploit this vulnerability. The specific flaw exists due to an information leak when querying the AWSI service which listens by default on TCP port 8039. The leak allows attackers to glean the security token of any remote machine. Once obtained this token can be added to the attackers registry and any objects the target has in the eDirectory tree can be accessed. The vulnerability lies in the combination of the ability to query the Desktop Management server for a remote clients workstation token and the lack of checking the token against the proper host.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/viewContent.do?externalId=7004945&sliceId=1

## Disclosure Timeline

- 2009-03-26 - Vulnerability reported to vendor
- 2009-11-30 - Coordinated public release of advisory
