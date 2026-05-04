# ZDI-10-301: Trend Micro Control Manager Server-agent Communication Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-301
- **ZDI-CAN:** ZDI-CAN-995
- **Date:** 2010-12-17
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Trend Micro
- **Affected Products:** Control Manager
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-301/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Trent Micro Control Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within how the mrf.exe component composes a string used to display an error message. The application will build the string using a buffer located on the stack using a sprintf call. As attacker controlled data is used to construct the string, this can lead to code execution under the context of the application.

## Additional Details

http://esupport.trendmicro.com/solution/en-us/1057059.aspx http://www.trendmicro.com/ftp/documentation/readme/readme_critical_patch_TMCM55_1318.txt -- Critical patch for SPNT regarding this VC. Available on download website. sp-tmi-580-win-en-criticalpatch2.exe http://www.trendmicro.com/ftp/products/patches/sp_tmi_580_win_en_criticalpatch2.exe ReadMe http://www.trendmicro.com/ftp/documentation/readme/sp_tmi_580_win_en_criticalpatch2_readme.txt

## Disclosure Timeline

- 2010-11-09 - Vulnerability reported to vendor
- 2010-12-17 - Coordinated public release of advisory
