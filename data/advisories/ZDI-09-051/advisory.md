# ZDI-09-051: EMC Replication Manager Client Control Service Remove Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-051
- **ZDI-CAN:** ZDI-CAN-451
- **Date:** 2009-08-07
- **CVE:** N/A
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** EMC
- **Affected Products:** Replication Manager
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-051/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the EMC Replication Manager Client. Authentication is not required to exploit this vulnerability. The specific flaw exists within the irccd.exe process which listens by default on a TCP port around 6700. The XML-based protocol this service communicates over accepts a RunProgram message. By supplying a malicious payload and requesting this functionality a remote attacker can execute arbitrary code on the remote system.

## Additional Details

The fixes and advisory are available to customers at powerlink.emc.com <http://powerlink.emc.com/>.

## Disclosure Timeline

- 2009-03-13 - Vulnerability reported to vendor
- 2009-08-07 - Coordinated public release of advisory
