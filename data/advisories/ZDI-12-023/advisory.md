# ZDI-12-023: Total Defense Suite UNC Management Web Service Database Credentials Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-023
- **ZDI-CAN:** ZDI-CAN-1123
- **Date:** 2012-02-08
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Total Defense
- **Affected Products:** CA Total Defense
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-023/
## Vulnerability Details

This vulnerability allows attackers to remotely obtain domain credentials on vulnerable installations of CA Total Defense Suite UNC Management Web Service. Authentication is not required to exploit this vulnerability. The specific flaw exists within the App_Code.dll service listening by default on TCP ports 34444 and 34443 (SSL). The service allows a remote client to request encrypted domain credentials without authentication. The encryption lacks a salt allowing an attacker with a local installation of CA Total Defense Suite UNC Management Web Service to easily decrypt the credentials.

## Additional Details

We are pleased to confirm that all three vulns that were reported by Tipping Point were proactively closed as part of the Total Defense R12 SE3 (Build 831) release cycle. This SE3 release is publicly shipping from our download links since December 5th, 2011. Physical media (DVD) is currently in production for those clients seeking that option as opposed to a download and we will be shipping those DVDs in early January 2012 based on the production schedule.

## Disclosure Timeline

- 2011-04-01 - Vulnerability reported to vendor
- 2012-02-08 - Coordinated public release of advisory
