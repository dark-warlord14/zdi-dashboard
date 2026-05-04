# ZDI-12-154: IBM Lotus Notes URL Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-154
- **ZDI-CAN:** ZDI-CAN-1343
- **Date:** 2012-08-22
- **CVE:** CVE-2012-2174
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** IBM
- **Affected Products:** Lotus Notes
- **Credit:** Moritz Jodeit
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-154/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM Lotus Notes. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within notes.exe. When handling URLs, it is possible to inject the -RPARAMS command line argument into the call to notes.exe, which will then launch rcplauncher.exe. Including the java -vm command will allow for the attacker to execute code under the context of the process.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: http://www-304.ibm.com/support/docview.wss?uid=swg21598348

## Disclosure Timeline

- 2011-12-22 - Vulnerability reported to vendor
- 2012-08-22 - Coordinated public release of advisory
