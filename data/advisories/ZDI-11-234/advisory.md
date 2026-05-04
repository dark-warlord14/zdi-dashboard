# ZDI-11-234: Trend Micro Control Manager CasLogDirectInsertHandler.cs Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-234
- **ZDI-CAN:** ZDI-CAN-1125
- **Date:** 2011-07-11
- **CVE:** N/A
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Trend Micro
- **Affected Products:** Control Manager
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-234/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Trend Micro Control Manager. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists within the Cas_LogDirectInsert.aspx http handler, which listens by default on TCP port 443. A specially crafted POST request allows remote attackers to supply XML and schema information which is used within queries to the backend database. By supplying malicious values, an attacker can inject themselves a user account which can be used to execute code via the management console on the service.

## Additional Details

http://esupport.trendmicro.com/solution/en-us/1058280.aspx Fix is posted at download center: tmcm-55-win-en-criticalpatch1422.exe http://downloadcenter.trendmicro.com/index.php?regs=NABU&clk=latest&clkval=1763&lang_loc=1 This critical patch resolves the following issue(s): Issue: A vulnerability allows an attacker to create and insert a user account which can be used to execute codes through the management console. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Solution: This critical patch imposes stricter rules for the insertion of system account relative tables to prevent attackers from inserting user accounts. Reference: http://www.trendmicro.com/ftp/documentation/readme/readme_critical_patch_TMCM55_1422.txt

## Disclosure Timeline

- 2011-04-01 - Vulnerability reported to vendor
- 2011-07-11 - Coordinated public release of advisory
