# ZDI-11-037: Symantec IM Manager Administrative Interface IMAdminSchedTask.asp Eval Code Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-037
- **ZDI-CAN:** ZDI-CAN-865
- **Date:** 2011-01-31
- **CVE:** CVE-2010-3719
- **CVSS:** 8.5
- **CVSS Vector:** AV:N/AC:M/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Symantec
- **Affected Products:** IM Manager
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-037/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Symantec IM Manager. Authentication is required to exploit this vulnerability in that a logged in user must be coerced into visiting a malicious link. The specific flaw exists within the ScheduleTask method exposed by the IMAdminSchedTask.asp page hosted on the web interface. This function does not properly sanitize user input from a POST variable before passing it to an eval call. An attacker can abuse this to inject and execute arbitrary ASP under the context of the user visiting the malicious link.

## Additional Details

Symantec has issued an update to correct this vulnerability. More details can be found at: http://www.symantec.com/business/security_response/securityupdates/detail.jsp?fid=security_advisory&pvid=security_advisory&year=2011&suid=20110131_00

## Disclosure Timeline

- 2010-10-12 - Vulnerability reported to vendor
- 2011-01-31 - Coordinated public release of advisory
