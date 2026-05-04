# ZDI-12-090: Symantec Web Gateway Shell Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-090
- **ZDI-CAN:** ZDI-CAN-1435
- **Date:** 2012-06-08
- **CVE:** CVE-2012-0297
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Symantec
- **Affected Products:** Web Gateway
- **Credit:** Tenable Network Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-090/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Symantec Web Gateway. Authentication is not required to exploit this vulnerability. The specific flaw exists due to insufficiently filtered user-supplied data used in a call to exec() in multiple script pages. The affected scripts are located in '/spywall/ipchange.php' and 'network.php'. There is also a flaw in '/spywall/download_file.php' that allows unauthenticated users to download and delete any file on the server.

## Additional Details

Symantec has issued an update to correct this vulnerability. More details can be found at: http://www.symantec.com/security_response/securityupdates/detail.jsp?fid=security_advisory&pvid=security_advisory&year=2012&suid=20120517_00

## Disclosure Timeline

- 2011-11-22 - Vulnerability reported to vendor
- 2012-06-08 - Coordinated public release of advisory
